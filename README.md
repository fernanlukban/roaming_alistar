
# Welcome to RoamingAlistar

RoamingAlistar is a League of Legends inhouse bot using discord-py and riotwatcher. It is heavily inspired by [Tolki](https://lol-data.com)'s inhouse bot which you can find [here](https://github.com/mrtolkien/inhouse_bot). This was initially created for the [Intercompany League of Legends (ICL)](https://discord.gg/QTBMHaf) discord server, where we play a lot of inhouses. If you're working for a tech company or just want to join a community for league, come check us out!

## Current Flow
The way we currently have inhouses setup is as follows
 - Someone notifies `@inhouse-notify` with a time and waits for people to react to the message
 - If enough people react to the message, a lobby is created, and a game is played
 - After the game is over, someone has to **manually** go to the web match history, **open up a developer console in chrome**, look for a **randomly named json file**, copy it, and paste it as a **.txt file** to an admin on discord
 - After the admin sees the message (which may or may not take a while), he/she has to take the json, add it to the pool of games, run a script, and screenshot the output and post it on the leaderboard standings

## Paint Points
It is really tedious to keep track of the games that are being played and subsequently making sure they were being uploaded into our stats leaderboard. I wanted something that would automated stats aggregation and leaderboard settings without the queueing that Tolki's bot has.

  

# Overview

RoamingAlistar

## Backend