from requests import get
import json
import discord
import json

def handle_build(message) -> discord.Embed:
    p_message = message.lower()
    data = json.loads(open("heroes.json", "r").read())
    
    if p_message == "bf":
        p_message = "blackfeather"
        
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

def handle_gpt():
    return "Not implemented yet"