import discord
from discord.ext import commands
from discord import app_commands
import responses
from keep_alive import keep_alive
from configs import TOKEN, API_KEY

def run_discord_bot():
  intents = discord.Intents.default()
  intents.message_content = True
  bot = commands.Bot(command_prefix='/', intents=intents)

  @bot.event
  async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} commands")

  @bot.tree.command(name="build", description = "Shows a build for a hero")
  @app_commands.describe(arg="Shows a build for a hero")
  async def build(interaction: discord.Interaction, arg: str):
    response = responses.handle_build(arg)
    await interaction.response.send_message(embed=response)

  @bot.tree.command(name="meme", description="Shows a random meme")
  @app_commands.describe()
  async def meme(interaction: discord.Interaction):
    response = responses.handle_meme()
    await interaction.response.send_message(embed=response)
  
  @bot.tree.command(name="abbreviations", description="Shows a list of abbreviations")
  @app_commands.describe()
  async def abbreviation(interaction: discord.Interaction):
    response = responses.handle_abbreviation()
    await interaction.response.send_message(embed=response)
        
  keep_alive()
  bot.run(TOKEN)