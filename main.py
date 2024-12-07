from disnake.ext import commands
from disnake import Intents, Status, Activity, ActivityType


async def main(TOKEN:str):
    intents = Intents.default()
    intents.message_content = True
    intents.reactions = True

    bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents)

    @bot.event
    async def on_ready():
        print("Ready")

    bot.load_extensions("./extensions/")
    bot.reload = True

    await bot.start(TOKEN)

if __name__ == "__main__":
    from asyncio import run

    TOKEN = open("token.txt", "r").read()
    run(main=main(TOKEN=TOKEN))