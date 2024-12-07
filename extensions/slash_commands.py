from disnake_plugins import Plugin
from disnake import CommandInteraction, TextChannel, Embed, Color
from json import dump, load

plugin = Plugin()

@plugin.slash_command(name="set-starboard-channel", description="Sets the starboard channel")
async def set_starboard_channel_interaction(inter:CommandInteraction, channel:TextChannel):
    with open("data.json", "r") as data_file:
        data = load(data_file)
    data["starboard-channel-id"] = channel.id

    with open("data.json", "w") as data_file:
        dump(data, data_file)
    
    await inter.response.send_message(embed=Embed(title="Starboard channel set", color=Color.green()))

@plugin.slash_command(name="set-starboard-threshold")
async def set_starboard_threshold_interaction(inter:CommandInteraction, threshold:int):
    if threshold < 1:
        await inter.response.send_message("Threshold must be an integer greater than 0")
        return
    
    with open("data.json", "r") as data_file:
        data = load(data_file)
    data["starboard-threshold"] = threshold

    with open("data.json", "w") as data_file:
        dump(data, data_file)
    
    await inter.response.send_message(embed=Embed(title="Starboard threshold set", color=Color.green()))

setup, teardown = plugin.create_extension_handlers()