# Mad Libs Game

**SITE OVERVIEW**
- - - 

This Mad Libs is a word game where the user has to enter some words (e.g. person’s name, noun, adjective, place, object etc.) and substitute these with blanks in a story. These word substitutions have a humorous effect when the resulting story is then read aloud. 

This Mad Libs Generator teaches to manipulate user-inputted data as the game refers to a series of inputs that a user enters. After all the inputs are entered the application takes all the data and arranges it to build a story template. This game is completely written in Python.

![Alternate text](/images/Responsive.png)

You can view the deployed website [here](https://mad-libs01.herokuapp.com/).

**UX**
- - -

The game is designed for kids and motivates them to think ouside the box when it comes to parts of speech. At the same time the game provides a fun way to use different words. Even though, the main target are children between 6 and 12 years old, adults as well can play and have fun with their kids or even by themself.

**User Stories**

As a user I want to be able to:

- Easily navigate between the different functions available in the application.
- Enjoy playing word game.
- Clearly understand how to interact with the application and get clear feedback for any action taken.

**FEATURES**
- - -

 Game Process
 
 - Upon launching the app a welcome message is      displayed. This identifies the name of the game: “The Mad Libs Game”.
 - User will be then asked if they want to start the game or leave it. If 'y' or ‘yes’ is pressed , the game will be displayed. If the user, instead, decides to enter ’n’ or ‘no’, the game will quit. 
 - No empty input field are allowed at any stage of the game. The user is provided with feedback on what has gone wrong and the question is asked again.
 - As first thing, the user is asked to enter his/her name. It can actually be any name, even a funny one, but all the characters entered have to be alphabets. Numbers or any other sign won’t be accepted. If the user enters an incorrect value an error message is displayed.
 - After the name, the user has to enter the age. Once again, only numbers are allowed and an error message will be displayed in case the player enters letters or signs.
 - Once name and age are entered, the user is asked to choose some words (e.g. noun, adjective, etc.) from a list of three options. The player can choose between one of them in order to complete the story. Considering the fact that the options are three, only numbers greater than 0 and lower than 3 can be accepted.
 - Finally the user has to enter a number and the name of two friends. Should any incorrect data be used, a feedback will be provided and the user asked again to enter the correct data.

 
 Feedback for invalid inputs

 - Mad Lib data input

 ![Alternate text](/images/Error.png)

 - Yes/no input

![Alternate text](/images/Error2.png)

Future Features

- I would like to add a choice of stories, so that the player can choose from a list with different themes.
- I am aware that the code written may not be the most efficient. I rather focused on creating solutions to build a fully functioning program with the code I learned and understand during the short space of time given for the course module completion and the project submission deadline. My idea would be to improve the interactivity of the program once I get more time and knowledge about Python.

- HTML: HTML has been used to give structure and content to the website.
- CSS: In order to style the content created with HTML, the CSS language has been used.
- Google Fonts: I used the Kanit and sans-serif font.
- Font Awesome: I used ther Font Awesome icons for the logo of the game located at the left of the heading.
- Pixabay: I used this platform for the images of the flags.
- Balsamiq Wireframes: I used it to produce low fidelity wireframes to organise the structure of the pages.

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
- [Python](https://www.online-python.com/) was used throughout the project's building/testing stage to troubleshoot for errors.
- The code has been validated through [PEP8 online](http://pep8online.com/). At the time of project submission, there were no errors detected in the PEP8 validator as below.

![Alternate text](/images/Validator.png)

Testing was performed using a MacBook Air (M1, 2020) on macOS Monterey with the following browsers:
- Google Chrome 102.0.5005.61
- Safari 15.3
- Mozilla Firefox 101.0.1

After testing the website I can confirm the project it's responsive in its all pages and works properly on all standard screen sizes.

The "Play" button is working in each section of the project. 
- In the Home Page the button starts the game. 
- In the Board Game/Game Area the button reset the score and starts a new game.


- BUGS

While on GitPod I was able to see the flags flashing in the Board Game, after the deployment, the live site was not showing the same results as on GitPod. Since I was refencing my images from my css file, I had to tell the server to come out of the css folder. Sorted fixing the path.

* VALIDATOR TESTING

HTML: No errors were returned when passing through the official W3C Validator. (https://validator.w3.org/nu/#textarea).

CSS: No errors were returned when passing through the official (Jigsaw) Validator (https://jigsaw.w3.org/css-validator/validator).

JavaScript: No errors were found on the website when using [JSHint Validator]https://jshint.com/ .

Accessibility: I generated a desktop and mobile report for the deployed site through the Google Chrome Dev Tools.

 - Home Page - Mobile
 ![Alternate text](/assets/images/lighthouse.png)
 - Home Page - Desktop
 ![Alternate text](/assets/images/lighthouse_desktop.png)

 
- UNFIXED BUGS

No unfixed bugs.

**DEPLOYMENT**
- - -
The site was deployed to GitHub Pages. The steps to deploy are as follows:

1. Navigate to my Github repository: https://github.com/LucaDP07/flags-game
2. In the GitHub repository navigate to the settings tab.
3. Select the pages link from the setting menu on the left hand side.
4. After selecting the main branch, the page provides the link to the completed website
The live link can be found here: https://lucadp07.github.io/flags-game/

**CREDITS**
- - - 

**Content**

- The Heading and the Logo were inspired by the [Love Maths](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LM101+2021_T1/courseware/2d651bf3f23e48aeb9b9218871912b2e/a8ec361b95e94c25bf8a821654bd57bc/?child=first) Project.

- The Timer structure was inspired by [WEB CIFAR](https://www.youtube.com/c/WEBCIFAROfficial).

- The Score Area was inspired by the [Love Maths](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LM101+2021_T1/courseware/2d651bf3f23e48aeb9b9218871912b2e/a8ec361b95e94c25bf8a821654bd57bc/?child=first) Project.

- The Javascript code was inspired by the book [Get Coding](https://getcodingkids.com/the-book/).


**Media**

- The icon used for the logo was taken from [Font Awesome](https://fontawesome.com/).

- All fonts imported from [Google Fonts](https://fonts.google.com/).

- Screenshot under the section "site overview" was created with [Am I responsive](https://ui.dev/amiresponsive).

- Pictures used for the Game have been taken from [Pixabay](https://pixabay.com/).

- The wireframes have been created using [Balsamiq Wireframes](https://balsamiq.com/wireframes/).