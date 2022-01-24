# DnD

## By Alejandro Spara Dominguez

![Example of the application on multiple devices.]()

#### This project was developed for the third project with the Code Institute and the Full Stack Development course.

### [Click here to view Site.]()

### [Click here to view Repository.](https://github.com/AlexSD92/DnD)

# Table of Contents:

1. [Why](#Why)
2. [User Experience(UX)](#user-experience-UX)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Strategy](#strategy)
    4. [Scope](#scope)
    5. [Structure](#structure)
    6. [Skeleton](#skeleton)
        1. [Wireframes](#wireframes)
    7. [Surface](#surface)
        1. [Colours](#colors)
        2. [Typography](#typography)
        3. [Images and Icons](#images-and-icons)
        4. [Sounds](#sounds)
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
    4. [Observations](#observations)
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
2. Anyone insterested in playing a game in a similar style to dungeons and dragons.
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
4. A map.
5. Ability to pick up items. 


## Structure 
<!-- normally this would include header, footer etc., perhaps talk about the story structure or map structure/ -->

<!-- The website was described with a structure in mind to focus on the gameplay elements, such as the Simon Game itself, high scores and instructions. There are no background images and the font style is kept consistent to not distract from the core elements of the website. -->


## Skeleton

### Wireframes

Wireframes for the site can be viewed [here](assets/images/readme/wireframes).

## Surface

### Colors

### Typography

### Images and Icons

### Sounds

# Features

## Current Features

## Future Features

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

### Python Tests

## User Tests

- First time user:

- Returning User:

## Bugs and Fixes

## Observations

# Deployment

## Cloning and Forking the GitHub Repository

In order to make changes to this code without affecting the original code, you must fork the repository. This means that you will be given a copy of the code for that moment in time. In order to do this, you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/DnD).
3. Near the top right, click 'Fork'.
4. A copy of the repository will be available for you to use within your own remote repositories.

In order to clone the code you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/DnD) you would like to clone.
3. Near the top, select 'Code' in the dropdown.
4. Copy the HTTPS address.
5. Navigate to the directory where you would like to create a new directory using the terminal.
    - Use the pwd command to know where you currently are.
    - Use cd followed by the directory name to change directories.
    - use mkdir followed by a new directory name to create a new directory.
6. Create a new directory (mkdir) named 'DnD'.
7. Change directory (cd) in to 'DnD.
8. Enter 'git clone https://github.com/AlexSD92/DnD.git'.
9. GitBash will clone the 'DnD' repository in to your chosen directory.

## Local Deployment

To develop your project locally, do the following:

1. Follow the above steps to either clone or fork the repository. 
2. Download the gitpod [extension](https://www.gitpod.io/docs/browser-extension/).
    - Feel free to use your IDE of choice, such as Atom, Gitbucket, etc.
3. Once in your own copy of the repository, click the green gitpod button to launch the project. 
4. Once loaded, head to the terminal and type 'python3 run.py' and press enter. 
5. The programme will now run. 

## Remote Deployment via Heroku

1. Follow the above steps to either clone or fork the repository.
2. Download the gitpod [extension](https://www.gitpod.io/docs/browser-extension/).
    - Feel free to use your IDE of choice, such as Atom, Gitbucket, etc.
3. Once in your own copy of the repository, click the green gitpod button to launch the project. 
4. If you add any dependencies to the project, make sure that you create a requirements file. 
    - 'use the pip3 freeze > requirements.txt' command to create this file.
5. Commit and push your changes to your repository. 
6. Head over to [Heroku](heroku.com) and create an account. 
    - Fill in the details on the form, for role you can select 'student'.
7. Once created, confirm your account by email and set your password.
8. Now that you have an account, click 'Create New App' and give it a name, and then select your region.
9. Head over to the 'Settings' tab and set up some Config Vars.
    - If you have any sensitive data, such as API credentials, you're going to need to specify that in your Config Vars. Create a config var and in the field, place your sensitive file information, for example, 'credentails.json'. Copy your entire file and past it into the field value and click 'Add'.
    - You can skip the the config vars step if you have no sensitive info to protect.
10. Within 'Settings' click on 'Add buildpack'.
    - Python is the first buildpack you need, so select that and click 'Save changes'.
    - Node.js is the second buildpack that you need, so select that and click 'Save changes'.
11. Click on the 'Deployment' section and then click on 'Github' to connect to Github.
    - Search for your repository and click 'connect' once you have found it. 
12. Set up automatic deploys so that Heroku will rebuild your app every time you push a new change to Github. 
    - You can choose to manually deploy if you wish.
13. Once the app is built, click the button to view your deployed app.
14. Happy testing.

# Credits

1. [W3Schools](https://www.w3schools.com/)
    - An invaluable resource for this project in terms of documentation and tutorials.

2. [MDN Web Docs](https://developer.mozilla.org/en-US/)
    - Another fantastic resource for this project in terms of documentation and tutorials.

3. [Stack Overflow](https://stackoverflow.com/)
    - Amazing forums with great and detailed discussions, not only demonstrating how to write code, but why it should be written that way.

4. [Code Institute](https://codeinstitute.net/)
    - Fantastic learning platform and amazing tutors on slack that are always willing to help.

5. Chris Quinn, Mentor
    - Excellent resource and a wealth of knowledge and insight. Lessons around CSS grid really added some invaluable knowledge and experience to my project.

---

[RETURN TO THE TOP](#DnD)
