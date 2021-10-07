import os
# Imports flash library
from flask import (Flask, flash, render_template,
                   redirect, request, session, url_for)
# Imports PyMongo database library
from flask_pymongo import PyMongo
# Imports object id used for tracing ID's to edit ect later
from bson.objectid import ObjectId
# Imports werkzeug to encrypt the user's passwords
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    # Allows connection to landing page
    return render_template("index.html")


@app.route("/all_trumps_showcase")
def all_trumps_showcase():
    # Gets all the cards from the database
    cards = mongo.db.trump_card_stats.find()
    # Allows connection to the showcase page
    return render_template("showcase.html", cards=cards)


@app.route("/register", methods=["GET", "POST"])
def register():
    # Checks if a form is being submitted
    if request.method == "POST":
        # Checks if the username is already in use
        existing_user = mongo.db.user_info.find_one(
            {"username": request.form.get("username").lower()})

        # Lets the user know it is taken
        if existing_user:
            flash("This username is already taken.")
            return redirect(url_for("register"))

        # Else the user's credentials are added to database
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        # Inserts into database
        mongo.db.user_info.insert_one(register)

        # Logs the user in
        session["user"] = request.form.get("username").lower()
        # Sends the user to their profile page
        return redirect(url_for("profile", username=session["user"]))
    # Allows the register page to be accessed
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # Checks if a form is being submitted
    if request.method == "POST":
        # Checks if the username exists
        existing_user = mongo.db.user_info.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Checks the password is correct
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    # Logs the user in
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                flash("Incorrect Username/Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username/Password")
            return redirect(url_for("login"))
    # Allows access to the login page
    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # gets the users username
    username = mongo.db.user_info.find_one(
        {"username": session["user"]})["username"]
    # protects against guessing URL's
    if session["user"]:
        cards = mongo.db.trump_card_stats.find()
        return render_template("profile.html", username=username, cards=cards)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Logs the user out by removing cookie
    session.pop("user")
    return redirect(url_for("all_trumps_showcase"))


@app.route("/card_maker", methods=["GET", "POST"])
def card_maker():
    # Checks if a form is being submitted
    if request.method == "POST":
        # gets all the key pairs for card creation
        data = {
            "card_name": request.form.get("card_name"),
            "image_url": request.form.get("image_url"),
            "attack_stat": request.form.get("attack_stat"),
            "defence_stat": request.form.get("defence_stat"),
            "speed_stat": request.form.get("speed_stat"),
            "charisma_stat": request.form.get("charisma_stat"),
            "luck_stat": request.form.get("luck_stat"),
            "card_maker": session["user"]
        }
        # Inserts card into database
        mongo.db.trump_card_stats.insert_one(data)
        return redirect(url_for("all_trumps_showcase"))
    return render_template("card_maker.html")


@app.route("/edit_card/<card_id>", methods=["GET", "POST"])
def edit_card(card_id):
    # Checks if a form is being submitted
    if request.method == "POST":
        # gets all the key pairs of the card
        data = {
            "card_name": request.form.get("card_name"),
            "image_url": request.form.get("image_url"),
            "attack_stat": request.form.get("attack_stat"),
            "defence_stat": request.form.get("defence_stat"),
            "speed_stat": request.form.get("speed_stat"),
            "charisma_stat": request.form.get("charisma_stat"),
            "luck_stat": request.form.get("luck_stat"),
            "card_maker": session["user"]
        }
        # Saves the new card values
        mongo.db.trump_card_stats.update({"_id": ObjectId(card_id)}, data)
        return redirect(url_for("all_trumps_showcase"))
    # resets the card
    card = mongo.db.trump_card_stats.find_one({"_id": ObjectId(card_id)})
    return render_template("edit_card.html", card=card)


@app.route("/delete_card/<card_id>")
def delete_card(card_id):
    # deletes a card
    mongo.db.trump_card_stats.remove({"_id": ObjectId(card_id)})
    return redirect(url_for("all_trumps_showcase"))


if __name__ == "__main__":  # Sets up sensitive user info
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
