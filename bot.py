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

  @bot.tree.command(name="comment", description="Shows a comment from a user")
  @app_commands.describe(arg="Shows a memorable comment from a user")
  async def comment(interaction: discord.Interaction, arg: str):
    response = responses.handle_comment(arg)
    await interaction.response.send_message(embed=response)
    
  @bot.command(name="addcomment", description="Adds a comment to a user")
  async def addcomment(ctx):
    if ctx.message.reference:
      replied_to_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
      username = replied_to_message.author.name
      message = replied_to_message.content
      response = responses.handle_addcomment(username, message)
      await ctx.send(embed=response)
    else:
      await ctx.send("This command must be a reply to a message.")
      
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
    
  @bot.tree.command(name="commands", description="Shows a list of commands")
  @app_commands.describe()
  async def list_commands(interaction: discord.Interaction):
    response = responses.handle_commands()
    await interaction.response.send_message(embed=response)
    
  @bot.tree.command(name="help", description="Shows a list of commands")
  @app_commands.describe()
  async def list_commands(interaction: discord.Interaction):
    response = responses.handle_commands()
    await interaction.response.send_message(embed=response)
  
  @bot.tree.command(name="repo", description="Output the github repo of the project")
  @app_commands.describe()
  async def repo(interaction: discord.Interaction):
    response = responses.handle_repo()
    await interaction.response.send_message(embed=response)
  
  @bot.tree.command(name="emojis", description="Shows a list of emojis")
  @app_commands.describe()
  async def emojis(interaction: discord.Interaction):
    response = responses.handle_emojis()
    await interaction.response.send_message(embed=response)
  
    
        
  keep_alive()
  bot.run(TOKEN)