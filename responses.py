import json
import discord
from requests import get
import random
import os
import shutil

def create_embed(title, description=None, url=None):
    embed = discord.Embed(title=title, description=description, url=url, color=0x00ff00)
    embed.set_footer(text="Made by: @nilasedits")
    return embed

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
        embed = create_embed(response)
        embed.add_field(name="", value="".join(output), inline=False)
    else:
        embed = create_embed(f"The input '{message}' is not a valid hero name.")
        
    return embed

def handle_meme():
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content)
    meme = create_embed(data['title'])
    meme.set_image(url=data['url'])
    return meme

def handle_abbreviation():
    data = load_json("abbreviations.json")
    embed = create_embed("Abbreviations")
    
    # Items
    items = data["items"]
    items_values = "\n".join(f"{item_short}: {item_full}" for item_short, item_full in items.items())
    embed.add_field(name="Items", value=items_values, inline=True)

    # Stats / Values / Attributes
    stats = data["stats"]
    stats_values = "\n".join(f"{stat} - {descriptions}" for stat, descriptions in stats.items())
    embed.add_field(name="Stats / Attributes", value=stats_values, inline=True)
    
    # Heroes
    heroes = data["heroes"]
    heroes_values = "\n".join(f"{hero_short}: {hero_full}" for hero_short, hero_full in heroes.items())
    embed.add_field(name="Heroes", value=heroes_values, inline=False)
    
    return embed

def handle_commands():
    data = load_json("commands.json")
    commands = data["commands"]
    embed = create_embed("Commands")
    field_value = "\n".join(f"{command}: {description}" for command, description in commands.items())
    embed.add_field(name="", value=field_value, inline=False)
    return embed

def handle_repo():
    embed = create_embed("Github Repo", url="https://github.com/NevermindNilas/Vainglory-Bot", description="The github repo for this project.")
    return embed

def handle_emojis():
    data = load_json("heroes.json")
    emojis = data["emojis"]
    embed = create_embed("Emojis")
    emojis_values = "\n".join(f"{emoji}: {description}" for emoji, description in emojis.items())
    embed.add_field(name="", value=emojis_values, inline=False)
    return embed

def handle_comment(message):
    data = load_json("comments.json")
    lower_message = message.lower()
    
    if lower_message in data:     
        comments = data[lower_message]
        # Select a random comment
        comment = random.choice(comments)
        embed = create_embed(f"{message} once said:")
        embed.add_field(name="", value=comment, inline=False)
    else:
        embed = create_embed(f"The user '{message}' does not have a memorable comment.")
    
    return embed

counter = 0
def handle_addcomment(username, message):
    global counter
    comments = load_json("comments.json")

    if username in comments:
        comments[username].append(message)
    else:
        comments[username] = [message]

    with open("comments.json", "w") as file:
        json.dump(comments, file)

    counter += 1
    if counter == 10:
        if not os.path.exists("backup"):
            os.makedirs("backup")
        shutil.copy2("comments.json", "backup/comments_backup.json")
        counter = 0

    embed = create_embed(title="Success", description=f"Added comment from **{username}**: {message}")

    return embed