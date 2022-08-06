import revolt
import asyncio
import aiohttp
from revolt.ext import commands
from random import randint
from mcstatus import server
import PyPixel
from mojang import MojangAPI
import dotenv
import os

config = dotenv.dotenv_values(".env")

dotenv.load_dotenv()


class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "mc!"

    @commands.command(name='server')
    async def server(self, ctx: commands.Context, ip):
        try:
            USE_QUERY = False
            mcServer = server.JavaServer.lookup(str(ip))
            mcStatus = mcServer.status()
            for i in range(len(os.getenv("QUERY_SERVERS"))):
                if os.getenv("QUERY_SERVERS")[i] == ip:
                    USE_QUERY = True
            if USE_QUERY == True:
                try:
                    mcQuery = mcServer.query()
                    if len(mcQuery.players.names) < 11:
                        playerNames = ""
                        for name in range(len(mcQuery.players.names)):
                            if name + 1 == len(mcQuery.players.names):
                                playerNames = playerNames + "{}".format(str(mcQuery.players.names[name]))
                            else:
                                playerNames = playerNames + "{}, ".format(str(mcQuery.players.names[name]))
                        pluginNames = ""
                        for plugin in range(len(mcQuery.software.plugins)):
                            if plugin + 1 == len(mcQuery.software.plugins):
                                pluginNames = pluginNames + "{}".format(str(mcQuery.software.plugins[plugin]))
                            else:
                                pluginNames = pluginNames + "{}, ".format(str(mcQuery.software.plugins[plugin]))
                        readableMOTD = mcQuery.motd.replace("§0", "").replace("§1", "").replace("§2", "").replace("§3", "").replace("§4", "").replace("§5", "").replace("§6", "").replace("§7", "").replace("§8", "").replace("§9", "").replace("§a", "").replace("§b", "").replace("§c", "").replace("§d", "").replace("§e", "").replace("§f", "").replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "").replace("\n", "")



                        await ctx.send("""Latency: {} ms
                        MOTD: {}
                        Minecraft Version: {}
                        Plugins: {}
                        Players Online: {}/{} ({})
                        This server has query enabled so there a a bit more information!""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(pluginNames), str(mcQuery.players.online), str(mcQuery.players.max), str(playerNames)))
                    else:
                        readableMOTD = mcQuery.motd.replace("§0", "").replace("§1", "").replace("§2", "").replace("§3", "").replace("§4", "").replace("§5", "").replace("§6", "").replace("§7", "").replace("§8", "").replace("§9", "").replace("§a", "").replace("§b", "").replace("§c", "").replace("§d", "").replace("§e", "").replace("§f", "").replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "").replace("\n", "")
                        await ctx.send("""Latency: {} ms
                        MOTD: {}
                        Minecraft Version: {}
                        Plugins: {}
                        Players Online: {}/{}
                        This server has query enabled so there is a bit more information!""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(mcQuery.software.plugins), str(mcQuery.players.online), str(mcQuery.players.max)))

                except:
                    LookupError
                    readableMOTD = mcStatus.description.replace("§0", "").replace("§1", "").replace("§2", "").replace("§3", "").replace("§4", "").replace("§5", "").replace("§6", "").replace("§7", "").replace("§8", "").replace("§9", "").replace("§a", "").replace("§b", "").replace("§c", "").replace("§d", "").replace("§e", "").replace("§f", "").replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "").replace("\n", "")
                    await ctx.send("""Latency: {} ms
                        MOTD: {}
                        Minecraft Version: {}
                        Players Online: {}/{}
                        WARNING: This server was listed to have query enabled but it didn't so there is no additional info.""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(mcStatus.players.online), str(mcStatus.players.max)))
            else:
                readableMOTD = mcStatus.description.replace("§0", "").replace("§1", "").replace("§2", "").replace("§3", "").replace("§4", "").replace("§5", "").replace("§6", "").replace("§7", "").replace("§8", "").replace("§9", "").replace("§a", "").replace("§b", "").replace("§c", "").replace("§d", "").replace("§e", "").replace("§f", "").replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "").replace("\n", "")
                await ctx.send("""Latency: {} ms
                    MOTD: {}
                    Minecraft Version: {}
                    Players Online: {}/{}""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(mcStatus.players.online), str(mcStatus.players.max)))
        except:
            LookupError
            await ctx.send("Sorry, an error occured. This usually happens when a server does not is exist or is currently offline.")
    @commands.command(name="hypixel")
    async def hypixel(self, ctx: commands.Context, player):
        try:
            hyp = PyPixel.Hypixel(api_key=os.getenv("HYPIXEL_API_KEY"))
            playerUUID = await hyp.get_uuid(str(player))
            player = await hyp.get_player(playerUUID)
            await ctx.send("""Rank: {}
            Last Online: {}
            Recently Played: {}
            First Login: {}
            Level: {}
            Achievment Points: {}
            Skywars Level: {}
            Karma: {}""".format(str(player.rank), str(player.last_logout), str(player.recently_played), str(player.firstLogin), str(player.level), str(player.achievement_points), str(player.stats.skywars.level), str(player.karma)))
        except:
            PyPixel.PlayerNotFound
            await ctx.send("Player not found! (OR an error has occurred)")
    @commands.command(name="player")
    async def player(self, ctx: commands.Context, player):
        playerUUID = MojangAPI.get_uuid(str(player))
        try:
            if not playerUUID:
                await ctx.send("Player not found!")
            else:
                player = MojangAPI.get_profile(playerUUID)
                await ctx.send(f"""UUID: {playerUUID}
                Skin: [Skin URL]({player.skin_url})
                """)
        except:
            await ctx.send("An error has occurred!")




async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, os.getenv("TOKEN_REVOLT"))
        await client.start()


asyncio.run(main())
