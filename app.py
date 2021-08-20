import os
from flask import (Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    return render_template("index.html")


@app.route("/all_trumps_showcase")
def all_trumps_showcase():
    cards = mongo.db.trump_card_stats.find()
    return render_template("showcase.html", cards = cards)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.user_info.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username is already taken.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.user_info.insert_one(register)

        session["user"] = request.form.get("username").lower()
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.user_info.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for("profile", username=session["user"]))
            else:
                flash("Incorrect Username/Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username/Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.user_info.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("all_trumps_showcase"))


@app.route("/card_maker")
def card_maker():
    return render_template("card_maker.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), 
            port=int(os.environ.get("PORT")),
            debug=True)