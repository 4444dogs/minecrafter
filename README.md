# About
Minecrafter is a Revolt bot for all things Minecraft!

Main Instance Invite: https://app.revolt.chat/bot/01G873ZAKVXGHT8TE28EENDZ5V

## Current Features
* Lookup online Minecraft servers
* Lookup Hypixel players



# Self-hosting
Do you want more ways to configure Minecrafter, or just test out your contributions? Well than this tutorial is for you! Please note that this tutorial assumes that you have already created your Revolt bot on the frontend.

## Requirements
* Python 3.10.5
* `revolt.py`, `mcstatus`, `PyPixel`, `mojang`, `mcrcon`, and `python-dotenv`

## Setup
1. Run `cp .env.example .env` (`cp` is replaced with `copy` on Windows.)
2. Replace `YOUR REVOLT TOKEN HERE` with your Revolt bot's token.
3. Get a Hypixel API token by running `/api` in the official Hypixel Minecraft server.
4. Replace `YOUR HYPIXEL API TOKEN HERE` with your new Hypixel API Token.
5. Run `python main.py` or `python3.10 main.py` depending on your operating system.
6. Enjoy!

## Additional Notes
If you know of a Minecraft server that has `enable-query` set to `true` then you can add it's IP in the form of a string to the `QUERY_SERVERS` list in `.env`

If you would like to connect to your Minecraft server's RCON you can follow the instructions below. (Note that to enter credentials for your server in `.env`, the credentials MUST all be in the same slot in the list.)
1. Add the channel that you wish to dedicate to RCON's id in the form of a string to the `RCON_CHANNELS` list in `.env`
2. Add your server's IP in the form of a string to the `RCON_IPS` list in `.env`
3. Add your server's RCON passsword in the form of a string to the `RCON_PASSWORDS` list in `.env`
4. Add any user that you wish to give RCON access to's Revolt ID in the form of a string to the `RCON_USERS` list in `.env`

