import discord
from discord.ext import commands
import os

# Bot Setup
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Bot ist online: {bot.user}")

@bot.slash_command(name="ping", description="Test-Command")
async def ping(ctx):
    await ctx.respond("Pong! Demokratie gesichert ✅")

# Bot starten mit Token aus den Railway-Variables
bot.run(os.getenv("TOKEN"))
