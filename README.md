# Discord-Bot
> Discord Bot project using Replit, Python. It incorporates API and API calls for one of its many command based interactions.

## Introduction

- Bots are powerful on Discord, offering a range of customizations for servers. Discord server owners install bots on servers to help moderate them or offer mini-games or features to their communities. 
- This project here aims to build a discord bot from scratch which performs functions and gives the users in the discord server to have access to some commands and can be customized to do various other functions within its reach. The project requirements and software used are replit and discord application. 
- We have implemented commands that allows the user to access the link to a Browser, allows the user to be a click away from YouTube music, be updated with the current news around the world etc…

## Software Requirements

- Operating System: Windows 10 or above
- Programming language: Python 
- Back end Development: Replit Database
- Code  editor: VS code & Replit

## Approach

Discord bots can be majorly coded using JavaScript and python, for this project we will be using python through and through.

At first we create a bot application in the Discord Developer portal under our username, we later authorize the bot with several functionalities such reading messages on the server,, moderating members, Banning members, usage of emojis and gifs etc…

Once we are done with adding the salient authorizations to the bot, we copy the Token of the bot that will be given to us. This token will be used in the code to attach our code to the specific bot that we’ve created. We add the bot to the servers where its presence is required and where it wants to be used. The bot will then be ready to listen any command given to it from any of the servers that it has been added to.

In our code, we will be importing a specific module for the development of this application. Python offers a Discord module to make it easy for developers to develop discord bots. This module contains several commands and functionalities that are not available in the bare python language.

We use the offered functionalities to create commands for the bot which always precede with a ‘:’ and also have a certain level of interactivity between the member of the guilds and the bot.

We have implemented several commands such as: 

1.	;hello: command which receives a greet text with author mention from the bot.

2.	;google: command which receives a link to the google website.

3.	;news: command which receives a random news website link.

4.	;music: command which redirects user to YouTube music via a link.

5.	;inspire: command which receives a random quote and the author from an API (Zenquoutes.io API).

Added features such as warnings to members when they resort to use inappropriate language inside a guild is also added.

## References

- [Discord-Bot](https://www.youtube.com/watch?v=SPTfmiYiuok) - Creating and Customising a Discord Bot 
- [API Documentation](https://premium.zenquotes.io/zenquotes-documentation/) - API used in the Discord Bot
