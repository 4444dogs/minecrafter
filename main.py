import mcstatus
import revolt
import asyncio
import aiohttp
from revolt.ext import commands
from random import randint
from mcstatus import server
import TOKENFILE

class Client(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "mc!"

    @commands.command(name='info')
    async def info(self, ctx: commands.Context, ip):
        try:
            mcServer = server.JavaServer.lookup(str(ip))
            mcStatus = mcServer.status()
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
                    Players Online: {}/{} ({})""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(pluginNames), str(mcQuery.players.online), str(mcQuery.players.max), str(playerNames)))
                else:
                    readableMOTD = mcQuery.motd.replace("§0", "").replace("§1", "").replace("§2", "").replace("§3", "").replace("§4", "").replace("§5", "").replace("§6", "").replace("§7", "").replace("§8", "").replace("§9", "").replace("§a", "").replace("§b", "").replace("§c", "").replace("§d", "").replace("§e", "").replace("§f", "").replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "").replace("\n", "")
                    await ctx.send("""Latency: {} ms
                    MOTD: {}
                    Minecraft Version: {}
                    Plugins: {}
                    Players Online: {}/{}""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(mcQuery.software.plugins), str(mcQuery.players.online), str(mcQuery.players.max)))

            except:
                LookupError
                readableMOTD = mcStatus.description.replace("§0", "").replace("§1", "").replace("§2", "").replace("§3", "").replace("§4", "").replace("§5", "").replace("§6", "").replace("§7", "").replace("§8", "").replace("§9", "").replace("§a", "").replace("§b", "").replace("§c", "").replace("§d", "").replace("§e", "").replace("§f", "").replace("§k", "").replace("§l", "").replace("§m", "").replace("§n", "").replace("§o", "").replace("§r", "").replace("\n", "")
                await ctx.send("""Latency: {} ms
                    MOTD: {}
                    Minecraft Version: {}
                    Players Online: {}/{}
                    WARNING: This server does not have query enabled so some of Minecrafter's features are not available for this server.""".format(str(mcStatus.latency), str(readableMOTD), str(mcStatus.version.name), str(mcStatus.players.online), str(mcStatus.players.max)))

        except:
            LookupError
            await ctx.send("Sorry, an error occured. This usually happens when a server does not is exist or is currently offline.")




async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, TOKENFILE.TOKEN_REVOLT)
        await client.start()


asyncio.run(main())
