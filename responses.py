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
    else:
        embed = discord.Embed(title=f"The input '{message}' is not a valid hero name.")
        
    embed.set_footer(text="Made by: @nilasedits")
    return embed


def handle_meme():
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}").set_image(url=f"{data['url']}")
    return meme

def handle_abbreviation():
    data = json.loads(open("abbreviations.json", "r").read())
    embed = discord.Embed(title="Abbreviations")
    
    # Items
    items = data["items"]
    items_values = ""
    for item_short, item_full in items.items():
        items_values += f"{item_short}: {item_full}\n"
        
    embed.add_field(name="Items", value=items_values, inline=True)

    # Stats / Values / Attributes
    stats = data["stats"]
    stats_values = ""
    for stat, descriptions in stats.items():
        stats_values += f"{stat} - {descriptions}\n"

    embed.add_field(name="Stats / Attributes", value=stats_values, inline=True)
    
    # Heroes
    heroes = data["heroes"]
    heroes_values = ""
    for hero_short, hero_full in heroes.items():
        heroes_values += f"{hero_short}: {hero_full}\n"
    
    embed.add_field(name="Heroes", value=heroes_values, inline=False)
    
    
    embed.set_footer(text="Made by: @nilasedits")
    return embed

def handle_commands():
    data = load_json("commands.json")
    commands = data["commands"]
    embed = discord.Embed(title="Commands")
    field_value = ""
    for command, description in commands.items():
        field_value += f"{command}: {description}\n"
    embed.add_field(name="", value=field_value, inline=False)
    embed.set_footer(text="Made by: @nilasedits")
    return embed

def handle_repo():
    embed = discord.Embed(title="Github Repo", url="https://github.com/NevermindNilas/Vainglory-Bot", description="The github repo for this project.")
    embed.set_footer(text="Made by: @nilasedits")
    
    return embed

def handle_emojis():
    # Print emojis cuz why not
    data = load_json("heroes.json")
    emojis = data["emojis"]
    embed = discord.Embed(title="Emojis")
    emojis_values = ""
    
    for emoji, description in emojis.items():
        emojis_values += f"{emoji}: {description}\n"
        
    embed.add_field(name="", value=emojis_values, inline=False)
    embed.set_footer(text="Made by: @nilasedits")
    return embed