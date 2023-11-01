from requests import get
import json
import discord
import json

def handle_build(message) -> discord.Embed:
    p_message = message.lower()
    data = json.loads(open("heroes.json", "r").read())
    
    if p_message == "bf":
        p_message = "blackfeather"
    elif p_message == "war":
        p_message = "warhawk"
    elif p_message == "grump":
        p_message = "grumpjaw"
    elif p_message == "silver":
        p_message = "silvernail"
        
    heroes = data["heroes"]

    if p_message in heroes:
        output = heroes[p_message]
        response = f"The build for ***{p_message.capitalize()}*** is:"
        embed = discord.Embed(title=response)
        embed.add_field(name="", value="".join(output), inline=False)
        embed.set_footer(text="Made by: @nilasedits")
        return embed
    else:
        return discord.Embed(title=f"The input '{message}' is not a valid hero name.")

def handle_meme():
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}").set_image(url=f"{data['url']}")
    
    return meme

def handle_abbreviation():
    data = json.loads(open("abbreviations.json", "r").read())
    stats = data["stats"]
    values = data["value"]
    embed = discord.Embed(title="Abbreviations")

    field_value = ""
    for stat, value in zip(stats, values):
        field_value += f"{stat}: {value}\n"

    embed.add_field(name="Stats / Attributes", value=field_value, inline=False)
    
    embed.set_footer(text="Made by: @nilasedits")
    
    return embed
def handle_gpt():
    return "Not implemented yet"