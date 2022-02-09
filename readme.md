# DnD

## By Alejandro Spara Dominguez

#### This project was developed for the third project with the Code Institute and the Full Stack Development course.

### [Click here to the app.](https://text-based-adventure-game.herokuapp.com/)

### [Click here to view Repository.](https://github.com/AlexSD92/DnD)

# Table of Contents:

1. [Why](#Why)
2. [User Experience(UX)](#user-experience-UX)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Strategy](#strategy)
    4. [Scope](#scope)
3. [Features](#features)
    1. [Current Features](#current-features)
    2. [Future Features](#future-features)
4. [Technologies](#technologies)
    1. [Languages](#languages)
    2. [Other Technologies, Frameworks and Libraries](#other-technologies-frameworks-and-libraries)
5. [Testing](#testing)
    1. [Code Tests](#code-tests)
    2. [User Tests](#user-tests)
    3. [Bugs and Fixes](#bugs-and-fixes)
6. [Deployment](#deployment)
    1. [GitHub Pages](#github-pages)
    2. [Cloning and Forking the GitHub Repository](#cloning-and-forking-the-github-repository)
    3. [Local Deployment](#local-deployment)
    4. [Remote Deployment](#remote-deployment)
7. [Credits](#credits)

# Why

# User Experience (UX)

## Target Audience

1. Anyone interested in playing a text-based adventure game.
2. Anyone interested in playing a fantasy adventure game.
3. Anyone that enjoys a role playing game. 

## User Stories

- First time user:
    1. I would like to play a text-based adventure game.
    2. I would like to play a fantasy game.
    3. I would like to play a role playing game.

- Returning User:
    1. I would like to play the game again.
    2. I would like to play through different choices. 
    3. I would like to reach an alternative ending.
    4. I would like to play again using an alternative class.

## Strategy

Create an engaging text-based role playing fantasy adventure game where a players' decisions can lead to different pathways and endings throughout the game.

## Scope

1. Give the player a choice in character class when they begin the game (warrior, mage, etc.).
2. Include elements where the player has to manage their characters stats, such as health, magic power, etc.
3. A combat mechanic. 
4. Inventory management.
6. Currency & shopping.
5. Ability to pick up items.
6. Ability to use items. 
7. Levelling up. 
8. Ability to view stats. 

# Features

## Current Features

1. Choice in character class. 
2. Players gain experience in battle and level up. 
3. Enemies drop items, such as potions and ethers after defeat. 
4. Players can scavange to find money. 
5. Players can shop to purchase potions and ethers with the money they have earned.
6. Players can heal, either using magic, potions or ethers. 
7. Players can view and use their inventory.
8. Players can view their stats. 
9. Players can select between different pathways and experience the story in different ways.

## Future Features

1. Multiple party members. 
2. Weilding multiple items.
3. A strength and weakness system for both players and enemies. 
4. Status effects, such as poison, paralysis, etc. 
5. More interactions with the environment, such as eating foods, uncovering items. 
6. An in game map. 
7. Incorporation of more class objects, such as magic, defense, etc.

# Technologies

## Languages

- [Python](https://www.python.org/)

## Other Technologies, Frameworks and Libraries

- [GitHub](https://github.com/)
    - Provided a Remote repository for the application. Allowing for my coding to be backed up online as I go.

- [Gitpod](https://gitpod.io/)
    - Code editor used for this project.

# Testing

## Code Tests

### PEP8 Online

Code passes through [PEP8 Online](http://pep8online.com/) with no errors, warnings or issues.

### Manual Testing

- Invalid user input.
    - At all stages of the program, various incorrect user inputs were tested against. For example, random strings, numbers or randomly pressing enter.
    - All invalid user input is presented with 'please make a valid choice' and the program will no proceed until a valid choice is made. 

- All game options work.
    - Being an role playing game, there are several options to make at each stage in the story. Each of those options are mapped to different functions. 
    - At each stage in the game, each game option was tested to determine that it would behave as expected / predicted. 

- All functions work as expected. 
    - There are many functions that manipulate various class objects and story decisions. All functions behave as expected. 

### Python Tests

## User Tests

- First time user:
    - Player launches the application and selects what class they would like to be. They also enter their characters name and confirm that they would like to proceed what they have selected. They then arrive at the first story arc, which introduces the player controls, such as hunting for enemies, scavenging for coin, etc. The player progresses through the story by selecting the options that trigger the next phase in the story.

- Returning User:
    - Player returns to the game and launches the application. Player selects a different class than the one they selected for their first playthrough. Throughout the story the character is forced to play in a different style because the class they selected has different attributes. They also make different choices throughout the game that they didn't make previously.

## Bugs and Fixes

- 29/01/2022 (IDENTIFIED), 30/01/2022 (RESOLVED) - The player can heal over their original hp amount. There is no hp cap, so the player could give themselves infinit amounts of hp over the original hp level. Resolved by introducing a max hp and max mp variable to behave as a cap. The max variables level up with the other characters, but remain unaffected by potions, healing, etc. In this way, they were used as a reference as to what the max hp and mp should be per level. 

- 29/01/2022 (IDENTIFIED & RESOLVED) - The player would gain a level after each battle. Resolved by setting the exp back to 0 at each level and adding the difference. 

- 08/02/2022 (IDENTIFIED), 09/02/2022 (RESOLVED) - Regardless of how much experience the player earns, they will only go up one level. For example, if to reach level 4 required 4,000 experience and in a single encounter the player gains 4,000 experience, they will only go from level 1 to level 2. Resolved by introducing variables to manage the experience gained. For example, current experience, experience gained, combined experience, experience requirement and remaining experience after levelling up. The fucntion calculates how much experience is required for a single levelup, subtracts that from the total combined experience and loops it until the combined experience is less than the experience required. 

- 09/02/2022, - While the program is running through the enemy's turn, the user can input, which can result in prompting the user to make a valid choice when they take their turn. While the incorrect input is handled, it can be confusing to the player. 

# Deployment

## Cloning and Forking the GitHub Repository

In order to make changes to this code without affecting the original code, you must fork the repository. This means that you will be given a copy of the code for that moment in time. In order to do this, you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/DnD).
3. Near the top right, click 'Fork'.
4. A copy of the repository will be available for you to use within your own remote repositories.

In order to clone the repository, you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/DnD) you would like to clone.
3. Near the top, select 'Code' in the dropdown.
4. Copy the HTTPS address.
5. Navigate to the directory where you would like to create a new directory using the terminal.
    - Use the pwd command to know where you currently are.
    - Use cd followed by the directory name to change directories.
    - use mkdir followed by a new directory name to create a new directory.
6. Enter 'git clone https://github.com/AlexSD92/DnD.git'.
7. The repository will be cloned in to your chosen directory.

## Local Deployment

To deploy your project locally using Gitpod, do the following:

1. Follow the above steps to either clone or fork the repository. 
2. Download the Gitpod [extension](https://www.gitpod.io/docs/browser-extension/).
3. Once in your own copy of the repository, click the green gitpod button to launch the project. 
4. Once loaded, install PrettyTable by typing 'pip install PrettyTable' in the terminal.
4. Then, in the terminal, type 'python3 run.py' and press enter. 
5. The programme will now run locally.

## Remote Deployment

1. Follow the above steps to either clone or fork the repository.
2. Download the Gitpod [extension](https://www.gitpod.io/docs/browser-extension/).
3. Once in your own copy of the repository, click the green gitpod button to launch the project. 
4. If you add any dependencies to the project, make sure that you create a requirements file. 
    - For this particular project, PrettyTable and Colorama were used. 
    - 'use the pip3 freeze > requirements.txt' command to create this file.
    - Colorama won't be included automatically, and you will have to add this manually.
        - 'pip list' or 'pip freeze' to view installed packages
        - 'pip show (filename)' to get details, such as the version
        - For example, if you typed 'pip show colorama' it would show you what version
        - In the requirements.txt file you created, you would add 'colorama==0.4.4'
5. Commit and push your changes to your repository. 
6. Head over to [Heroku](heroku.com) and create an account. 
    - Fill in the details on the form, for role you can select 'student'.
7. Once created, confirm your account by email and set your password.
8. Now that you have an account, click 'Create New App' and give it a name, and then select your region.
9. Head over to the 'Settings' tab and to set up some Config Vars.
    - If you have any sensitive data, such as API credentials, you're going to need to specify that in your Config Vars. Create a config var and in the field, place your sensitive file information, for example, 'credentails.json'. Copy your entire file and past it into the field value and click 'Add'.
    - You can skip the the config vars step if you have no sensitive info to protect.
10. Within 'Settings' click on 'Add buildpack'.
    - Python is the first buildpack you need, so select that and click 'Save changes'.
    - Node.js is the second buildpack that you need, so select that and click 'Save changes'.
    - They must be in that order, Python then Node.js.
11. Click on the 'Deployment' section and then click on 'Github' to connect to Github.
    - Search for your repository and click 'connect' once you have found it. 
12. Set up automatic deploys so that Heroku will rebuild your app every time you push a new change to Github. 
    - You can choose to manually deploy if you wish.
13. Once the app is built, click the button to view your deployed app.
14. Happy testing.

# Credits

1. [W3Schools](https://www.w3schools.com/)
    - An invaluable resource for this project in terms of documentation and tutorials.

2. [Stack Overflow](https://stackoverflow.com/)
    - Amazing forums with great and detailed discussions, not only demonstrating how to write code, but why it should be written that way.

3. [Code Institute](https://codeinstitute.net/)
    - For their learning platform and support. 

4. Chris Quinn, Mentor
    - Excellent resource and a wealth of knowledge and insight.

---

[RETURN TO THE TOP](#DnD)
