import json
import discord
from requests import get

def load_json(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

def handle_build(message) -> discord.Embed:
    data = load_json("heroes.json")
    p_message = message.lower()

    name_map = {
        "bf": "blackfeather",
        "war": "warhawk",
        "grump": "grumpjaw",
        "silver": "silvernail",
        "nail": "silvernail"
    }
    
    p_message = name_map.get(p_message, p_message)

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
    values = data["values"]
    embed = discord.Embed(title="Abbreviations")

    # Stats / Values / Attributes
    field_value = ""
    for stat, value in zip(stats, values):
        field_value += f"{stat}: {value}\n"

    embed.add_field(name="Stats / Attributes", value=field_value, inline=False)
    
    # Heroes
    hero_shorts = data["hero_shorts"]
    hero_fulls = data["hero_fulls"]
    
    heroes_value = ""
    for hero_short, hero_full in zip(hero_shorts, hero_fulls):
        heroes_value += f"{hero_short}: {hero_full}\n"
    
    embed.add_field(name="Heroes", value=heroes_value, inline=False)
    
    embed.set_footer(text="Made by: @nilasedits")
    
    return embed
