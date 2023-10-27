from requests import get
import json
import discord

def handle_build(message) -> str:
    p_message = message.lower()
    emojis = {
        "Bonesaw": "<:emoji_32:1151165758487941191>",
        "SorrowBlade": "<:emoji_38:1151166970956353617>",
        "Tyrants_Monocle": '<:emoji_30:1151165291435405312>',
        "Tornado_Trigger": "<:emoji_31:1151165555915636817>",
        "Cooldown_Boots": "<:emoji_46:1151169123762577409>",
        "Breaking_Point": "<:emoji_34:1151166178249674752>",
        "Tension_Bow": "<:emoji_33:1151166013291909120>",
        "Cooldown_Sword": "<:emoji_36:1151166572099018813>",
        "Serpent_Mask": "<:emoji_37:1151166733776863315>",
        "Poisoined_Shiv": "<:emoji_35:1151166333325676696>"
    }
    
    heroes = {
        # Carries
        "ringo": [emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"], "\n", emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"]],
        "kestrel": [emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"], "\n", emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Serpent_Mask"], emojis["Breaking_Point"]],
        "gwen": [emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"], "\n", emojis["SorrowBlade"], emojis["Breaking_Point"]],
        "silvernail": [emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"]],
        "kensei": [emojis["Bonesaw"], emojis["Cooldown_Boots"], emojis["Breaking_Point"], emojis["Serpent_Mask"]," ", "(heavy steel and then bonesaw)", '\n', emojis["Bonesaw"], emojis["Cooldown_Boots"], emojis["Breaking_Point"], emojis["Poisoined_Shiv"], emojis["SorrowBlade"], " ", "(heavy steel and then bonesaw)"],
        "kinetic": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"]],
        "caine": ["<:caine:>"],
        "celeste": ["<:celeste:>"],
        "baron": [emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"]],
        "idris": ["<:idris:>"],
        "skaarf": ["<:skaarf:>"],
        "samuel": ["<:samuel:>"],
        "vox": [emojis["Poisoined_Shiv"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"], "\n", emojis["Poisoined_Shiv"], emojis["Cooldown_Boots"], emojis["SorrowBlade"], emojis["Bonesaw"], emojis["Breaking_Point"]],
        "varya": ["<:varya:>"],
        "ishtar": ["<:ishtar:>"],
        "leo": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"], "\n", emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Tension_Bow"], emojis["Breaking_Point"]],
        "saw": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"]],
        "miho": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"]],
        "warhawk": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"]],
        
        # Junglers
        "ylva": [emojis["Bonesaw"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"]],
        "skye": ["<:skye:>"],
        "alpha": ["<:alpha:>"],
        "blackfeather": ["<:blackfeather:>"],
        "baptiste": [emojis["Poisoined_Shiv"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["SorrowBlade"], emojis["Breaking_Point"], "\n"],
        "joule": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"]],
        "glaive": ["<:glaive:>"],
        "grumpjaw": [emojis["SorrowBlade"], emojis["Cooldown_Boots"], emojis["Poisoined_Shiv"], emojis["Bonesaw"], emojis["Breaking_Point"], "\n"],
        "krul": ["<:krul:>"],
        "koshka": ["<:koshka:>"],
        "ozo": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Bonesaw"], emojis["Breaking_Point"], "\n"],
        "petal": [emojis["Bonesaw"], emojis["Cooldown_Boots"], emojis["Tyrants_Monocle"], emojis["Tyrants_Monocle"], emojis["SorrowBlade"]],
        "reza": ["<:reza:>"],
        "reim": ["<:reim:>"],
        "rona": ["<:rona:>"],
        
        # Captains
        "adagio": [emojis["Serpent_Mask"], emojis["Cooldown_Boots"], emojis["Poisoined_Shiv"], emojis["Bonesaw"], emojis["Breaking_Point"], "\n",],
        "lorelai": ["<:lorelai:>"],
        "churnwalker": ["<:churnwalker:>"],
        "grace": ["<:grace:>"],
        "yates": ["<:yates:>"],
        "lyra": ["<:lyra:>"],
        "ardan": ["<:ardan:>"],
        "catherine": ["<:catherine:>"],
        "flicker": ["<:flicker:>"],
        "fortress": ["<:fortress:>"],
        "lance": ["<:lance:>"],
        "phinn": ["<:phinn:>"]
    }
    
    hero_name = next((hero for hero in heroes if hero in p_message), None)
    if hero_name is None:
        return ""
    
    hero_emojis = heroes[hero_name]
    response = f"The build for ***{hero_name.capitalize()}*** is:\n{''.join(hero_emojis)}"
    return response

def handle_meme():
    content = get("https://meme-api.com/gimme").text
    data = json.loads(content)
    meme = discord.Embed(title=f"{data['title']}").set_image(url=f"{data['url']}")
    
    return meme