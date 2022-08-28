import voltage
from voltage.ext import commands
import os
import dotenv

client = commands.CommandsClient("mc!")

config = dotenv.dotenv_values("../.env")

dotenv.load_dotenv()

@client.listen("ready")
async def on_ready():
    await client.set_status("""My prefix is "mc!" """, voltage.PresenceType.online)
    client.add_extension("cogs.minecraft")


client.run(os.getenv("TOKEN_REVOLT"))
