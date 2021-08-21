![webiste](readmeassets/amResponsiveMinefield.png)
# Top of the Trumps
## An Backend Development Project by Edward Stanley
'Top of the Trumps' is a database driven project using MongoDB for data storage and retrieval as well as Materialize for the styling and form elements. The website allows users to create their own cards based on the popular card game Top Trumps, the goal being the crossover of multiple characters and fandoms to create one large Top Trumps card depository.
Users have the ability to create their own private accounts in which they can create, edit and delete their creations whilst leaving the work of others untouched. 
#

## UX
## Different User objectives
### Site Owner's objectives
* The owner wants to create a community for creating Top Trumps cards
* The owner wants to create a pleasant website experience for the user

### Registered User objectives
* The user wants to be able to create a card modelled after the game 'Top Trumps'
* The user wants to be able to make changes to a card if necessary
* The user wants to be able to delete a card if necessary
* The user wants their creations to be safe from other people editing/deleting them
* The user wants to be able to see other creations in the community
* The user wants to be able to log in and out securely
* The user wants any data relating to IP ect to be kept private
* The user wants visual aids for the card statistics

### Unregistered User objectives
* The user wants to be able to create an account with a secure username/password
* The user might want to see community creations before registering

## User Stories
### As an owner:
* I want the site to have navigation controls for multiple devices
* I want the user to have as much control over their account as possible
* I want to create a site which credits community members who make content for it

### As a user:
* I want to be able to create my own cards including stats, graphics, and names
* I want to be able to create a unique account, and have full control over what content is in there
* I want to see what cards the community has created, and who created them
* I want a secure registration, log in, log out process using password encryption

#
## Wireframes
The following wirefrane was made in Balsamiq  
[Please Click Here.](readmeassets/milestonetwowireframe.pdf)

The wireframe can also be found in the readmeassets folder included in this project

#
## Features
### Existing Features
For the features I will go on a page to page basis.

### The Landing Page (index.html)
1) Has informative text letting the user know what the website is about
2) Has working buttons for registering and loging in, depending on the user's needs

### The Showcase Page (showcase.html)
1) Displays all the cards created by the community, each card displays the name of the card, the associated image, the statistics of the card based on 5 key values with accompanying bars for visual aid, and the username of the maker of the card

### The Login/Register Page (login.html/register.html)
1) Contains text fields for the user to input a username and password
2) If an error occurs such as a repeated username or wrong password a flash message is displayed notifying the user
3) A button which sends data to the database once conditions are fufilled which can write a new entry to the database, or check if the user's credentials are correct

### The Card Creation/Editing Page (card_maker.html/edit_card.html)
1) Contains multiple form inputs for the values of a card. The details are a text input for the name, a url input for the picture, sliders to adjust the stat values, and a button to write to the database or submit changes.
2) If editing, the current values of the card are automatically updated into the form.
3) Form validation notifies the user if something is wrong

### The Profile Page (profile.html)
1) Only displays the cards the user themselves have made
2) Adds buttons to the cards allowing for editing and deletion
3) Uses cookies to recognise which user is using the website and fetches their data accordingly

### The Base Page (base.html)
1) The template page which loads content from other pages into itself to display
2) A dropdown navbar full of links for accessing the website which updates its displayed values based on whether the user is logged in or not
3) A secondary navbar for smaller screens holding all the links allowing for small screen navigation
4) Contains the logo and main background for all pages

### Features Left to Implement
1) A way for the user to export their completed card as a png file
2) A way for users to 'subscribe' to other user's cards allowing them to add them into a custom deck in their profile
3) A game using those custom decks allowing users to play top trumps in browser

#
## Technologies Used
- HTML5 - Allows the website to be structured
- CSS - Allows styalising of elements to provide visual effect
- JQuery - Initialized the dropdown menu
- Python - Allowed database retrieveal, writing to, and editing. Also allowed for user accounts.
- Flask - An import that allowed better communication between Python and HTML
- [MaterializeCSS](https://materializecss.com/) - Allowed for implementation of form elements and CSS, as well as icons for visual effect
- [Gitpod](https://www.gitpod.io/) - The main coding platform used to create the project
- [Github](https://github.com/) - Allowed for the website to be deployed and version control
- [Gimp Studio](https://www.gimp.org/) - Allowed the editing of the background image for the website
#
## Testing
### HTML W3 Validator
 ![webiste](readmeassets/htmlvalidatorone.png)

 In order to check my HTML I put my website's URL into the validator. Whilst the majority was just issues with commenting which didn't affect the code, there was an odd interaction popping up between my last div in my footer. Upon further inspection I simply added a " in my div tags by mistake. Deleting it solved those errors.

 ![webiste](readmeassets/htmlvalidatortwo.png)
 ### CSS W3 Validator
 ![webiste](readmeassets/cssvalidatorresult.png)
 There was no problems with my CSS code, the validator passed it first time.
 ### JSHint Validator
 After putting the code through the validator there were multiple complaints about the 'let' initialiser however on closer inspection it was fine. The most that was wrong with the code was the occasional missing semi-colon which I fixed.
### Lighthouse Testing
![webiste](readmeassets/lighthousevalidator.png)
After running it through Google Chrome's lighthouse tool I had an overall result of 89 which was quite ideal. The page was able to load efficiently and effectively. 

### Larger issues through Testing
There were a couple of parts of the code which frustrated me for a while before finally working through to a solution:

### User Story Testing
##### *" Owner - I want the site to have controls for multiple devices (mouse and touchscreen controls). -"*
- There are optional buttons for mobile users allowing them to reveal/flag tiles as necessary. There are also alternate controls for mouse users in the form of right and left click readers to add ease of access.

##### *" User- I want to be able to play the game on any device"*
- The tiles are able to dynamically grow/shrink to fit any screen size allowing for a wide range of screen sizes to be used.

##### *" Owner - * I want the user to have as much control over their experience as possible"*
##### *" User- I want to be able to control as much of the games setup as possible"*
- The user is able to control their own diffculty through the Status Area dimension and bomb values. Their diffculty setting is essentially custom. The added functionality of the flagging also gives the user more control over the game.

##### *" User- I want the game to have quality of life features that handle any unecessary actions"*
- The game has a number of these in place. For example the auto reveal of tiles adjacent to a tile with no bombs near it speeds up the process for the user significantly especially with larger board sizes. The game also keeps track of key statistics for the user such as how many spaces they've flagged and how many tiles are left so the user doesn't have to calculate manually.

##### *" User - I want to have access to instructions on how to play"*
- The header features an external link to a page with instructions on how Minesweeper plays out.

##### *" User- I want to have graphics relevant to the game that clearly convey what is happening"*
- The use of coloured tiles in addition to the numbers on each tile creates an easier visual distinction for the user when playing the game. All colours are very different from eachother so confusion is minimum. The background graphic also doesn't distract from the game itself and the translucent overlay for containers makes text easier to read.

##### *" Owner - I want to create a game that visitors can enjoy used"*
- I myself very much enjoyed making and playing this game in browser

#
## Deployment
Before attempting to download this project for your own I highly recommend installing Python3, pip3 (which can be used to import other parts like flask), and setting up accounts on Heroku and MongoDB.

To deploy the website I used the following steps:



### How to run the project locally

#
## Credits
### External Code
Any external code used was from MaterializeCSS in order to structure the dropdown menu, forms, and general CSS styling. Everything python-side was what I had learnt from lessons/ my own logic.

### Media - photos
One photo was used for this project, and it was edited into the custom background by myself. The origional can be found[here.](https://imgbin.com/png/Gzs6cgcm/top-trumps-logo-winning-moves-png) 

## Acknowledgement
Thanks you for looking over this project, I hope you had a go at creating some cards of your own!
Thank you for your time.
#