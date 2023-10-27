from requests import get
import json
import discord
import json

def handle_build(message) -> str:
    p_message = message.lower()
    data = json.loads(open("heroes.json", "r").read())

    heroes = data["heroes"]

    if p_message in heroes:
        output = heroes[p_message]
        response = f"The build for ***{p_message.capitalize()}*** is:\n{''.join(output)}"
        return response
    else:
        return "The input is not a valid hero name."

def handle_meme():
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}").set_image(url=f"{data['url']}")
    
    return meme

build = handle_build("kensei")
print(build)