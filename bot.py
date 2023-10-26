import discord
import responses
from discord.ext import commands
from keep_alive import keep_alive
import os

async def send_message(message, user_message):
  try:
    response = responses.handle_build(user_message)
    await message.channel.send(response)

  except Exception as e:
    print(e)

async def send_meme(message):
  try:
    response = responses.handle_meme()
    await message.channel.send(embed=response)

  except Exception as e:
    print(e)

async def send_echta(message):
  try:
    response = responses.handle_echta()
    await message.channel.send(response)

  except Exception as e:
    print(e)

def run_discord_bot():
  TOKEN = f"{os.environ['DISCORD_SECRET']}" # Replace token with your own, if self hosted just put it in as a string.
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)
  bot = commands.Bot(command_prefix='!', intents=intents)

  @bot.command()
  async def hellou(ctx):
    await ctx.send('test')

  @client.event
  async def on_ready():
    print(f'{client.user} has connected to Discord!')

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f'{username}: {user_message} ({channel})')

    if user_message.startswith('!build') or user_message.startswith('!b'):
      await send_message(message, user_message)
    elif user_message.startswith('!meme'):
      await send_meme(message)
    '''if message.author.id == 393281695958433793:
            await send_echta(message)'''

  keep_alive()
  client.run(TOKEN)
