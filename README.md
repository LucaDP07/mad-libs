# Mad Libs Game

**SITE OVERVIEW**
- - - 

This Mad Libs is a word game where the user has to enter some words (e.g. person’s name, noun, adjective, place, object etc.) and substitute these with blanks in a story. These word substitutions have a humorous effect when the resulting story is then read aloud. 

This Mad Libs Generator teaches to manipulate user-inputted data as the game refers to a series of inputs that a user enters. After all the inputs are entered the application takes all the data and arranges it to build a story template. This game is completely written in Python.

![Alternate text](/images/Responsive.png)

You can view the deployed website [here](https://mad-libs01.herokuapp.com/).

**UX**
- - -

The game is designed for kids and motivates them to think ouside the box when it comes to parts of speech. At the same time the game provides a fun way to use different words. Even though the main target are children between 6 and 12 years old, adults as well can play and have fun with their kids or even by themself.

**User Stories**

As a user I want to be able to:

- Easily navigate between the different functions available in the application.
- Enjoy playing word game.
- Clearly understand how to interact with the application and get clear feedback for any action taken.

**FEATURES**
- - -

 Game Process
 
 - Upon launching the app a welcome message is      displayed. This identifies the name of the game: “The Mad Libs Game”.
 - User will be then asked if they want to start the game or leave it. If 'y' is pressed , the game will be displayed. If the user, instead, decides to enter ’n’, the game will quit. 
 - No empty input fields are allowed at any stage of the game. The user is provided with feedback on what has gone wrong and the question is asked again.
 - As first thing, the user is asked to enter his/her name. It can actually be any name, even a funny one, but all the characters entered have to be alphabets. Numbers or any other sign won’t be accepted. If the user enters an incorrect value an error message is displayed.
 - After the name, the user has to enter the age. Once again, only numbers are allowed and an error message will be displayed in case the player enters letters or signs.
 - Once name and age are entered, the user is asked to choose some words (e.g. noun, adjective, etc.) from a list of three options. The player can choose between one of them in order to complete the story. Considering the fact that the options are three, only numbers greater than 0 and lower than 3 or equal to three can be accepted.
 - Finally the user has to enter a number and the name of two friends. Should any incorrect data be used, a feedback will be provided and the user asked again to enter the correct data.

 
 Feedback for invalid inputs

 - Mad Lib data input

 ![Alternate text](/images/Error.png)

 - Yes/no input

![Alternate text](/images/Error2.png)

Future Features

- I would like to add a choice of stories, so that the player can choose from a list with different themes.
- I am aware that the code written may not be the most efficient. I rather focused on creating solutions to build a fully functioning program with the code I learned and understand during the short space of time given for the course module completion and the project submission deadline. My idea would be to improve the interactivity of the program once I get more time and knowledge about Python.

**TECHNOLOGIES**

- [Python](https://www.python.org/) was used to create the project.
- Time method is used to control the display speed to prevent the text displaying too fast.
- The Code Institute's [GitHub full template](https://github.com/Code-Institute-Org/python-essentials-template) for Python is used in order for the program to display properly in the deployed site on Heroku.
- [GitHub](https://github.com/) was used to host repository.
- [GitPod](https://www.gitpod.io/) was used to develop the project.
- [Heroku](https://dashboard.heroku.com/apps) was used to deploy the application and provides an environment in which the code can execute


**TESTING**
- - - 

- All input elements were tested to prevent user from entering unwanted data. Invalid data were entered to ensure that invalid user input returns appropriate feedback to the user.
- The code was tested using both GitPod terminal and the Heroku deployed site to ensure platform issues were not present in both displays.
- [Online Python](https://www.online-python.com/) was used throughout the project's building/testing stage to troubleshoot for errors.
- The code has been validated through [PEP8 online](http://pep8online.com/). At the time of project submission, there were no errors detected in the PEP8 validator as below.

![Alternate text](/images/Validator.png)


**DEPLOYMENT**
- - -
Deployment procedure

1. Ensure all code is correct and ready for deployment.
2. Enter the following code to import the required dependencies to the requirements.txt file:
- pip3 freeze > requirements.txt
- Heroku will use this file to import the dependencies that are required.

3. Sign up and log in to Heroku
4. Click on "Create new app" button.
5. In the next page displayed, enter the project name, and select Europe as region, then click "Create app" button.
6. Open settings page by pressing the settings tab. The following procedures have to be done in exact order. In the Buildpack section of the setting page, press Add Buildpack button and choose python then, click save changes. Select Add Buildpack button again and choose nodejs, then save changes
7. Navigate to deploy page by clicking the tab "Choose GitHub" then click "Connect to GitHub" button. In the popup window, click authorize and then input password for GitHub Once the Git Hub repositories are connected, type in to search for the project, mad-libs. When the repository is found, click connect button for the repository. The GitHub button indicates connected when connection was successful.
8. As I wanted to have control when to deploy the version, I have chosen manual deployment by pressing Deploy branch button instead of Enable Automatic Deploys.
9. Once the deployment was completed a View button will appear. This View button will open the terminal game in the new window. [Here](https://mad-libs01.herokuapp.com/) is the deployed page.
10. As manual deployment was chosen, I had to come back to Heroku deployment page whenever I have an updated working version pushed into the GitHub page.

**CREDITS**
- - - 

- At the initial stage of the project, [this page](https://www.youtube.com/watch?v=O1m_UIr7wOQ&t=588s) has been used to get a general guidance on how to approach the work.
- [Stack Overflow](https://stackoverflow.com/) was used to identify and resolve existing bugs.
- [Python in easy steps book](https://ineasysteps.com/products-page/python-easy-steps-2nd-edition/) was used as a general source for the code.
- [Online Python](https://www.online-python.com/) was used throughout the project's building/testing stage to troubleshoot for errors.

**MEDIA**
- - -

- The story for the mad lib was taken and adapted from the website [ReadBrightly](https://www.readbrightly.com/)

- Screenshot under the section "site overview" was created with [Am I responsive](https://ui.dev/amiresponsive).

