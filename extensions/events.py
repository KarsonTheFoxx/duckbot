from disnake_plugins import Plugin
from disnake import Embed, Color, Reaction, User, Message
from json import load, dump

plugin = Plugin()

@plugin.listener("on_reaction_add")
async def on_reaction_add(reaction:Reaction, _:User):
    with open("data.json", "r") as data_file:
        data = load(data_file)

    if not data["starboard-channel-id"]:
        return

    if reaction.count == data["starboard-threshold"] and reaction.emoji == "⭐":
        starboard_channel = reaction.message.guild.get_channel(data["starboard-channel-id"])

        await starboard_channel.send(
            content=reaction.message.author.mention,
            embed = Embed(
                title=f":star: Starboard #{data['starboard-count']+1}", 
                description=reaction.message.content, color=Color.random()).add_field(
                    name="Jump to message", 
                    value=reaction.message.jump_url).set_thumbnail(
                        url=reaction.message.author.avatar.url))

        data["starboard-count"] += 1
        with open("data.json", "w") as data_file:
            dump(data, data_file)

@plugin.listener("on_message")
async def on_message(message:Message):
    if not plugin.bot.user.mention in message.content:
        return
    
    if message.author.id == 242478407500300290:
        await message.reply("No.")
    else:
        await message.reply("Quack")

setup, teardown = plugin.create_extension_handlers()    
