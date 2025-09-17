import discord
from discord.ext import commands
import os

# Bot Setup
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Wenn Bot startet
@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")

# Slash Command: Helldivers Bericht
@bot.slash_command(name="helldivers_bericht", description="Erstelle einen Helldivers Einsatzbericht")
async def helldivers_bericht(
    ctx,
    planet: discord.Option(str, "Planet?"),
    sektor: discord.Option(str, "Sektor?"),
    gegner: discord.Option(str, "Gegner", choices=["Automaton", "Terminid", "Illuminate"]),
    mission: discord.Option(str, "Missionsziel?"),
    stratagems: discord.Option(str, "Stratagems/Ausrüstung"),
    helldiver: discord.Option(int, "Anzahl Helldiver", choices=[1, 2, 3, 4]),
    verluste: discord.Option(int, "Gefallene", choices=[0, 1, 2, 3, 4]),
    ausgang: discord.Option(str, "Ausgang", choices=["Erfolg", "Teil-Erfolg", "Fehlschlag"]),
    dauer: discord.Option(str, "Einsatzdauer (z. B. 45 Minuten)")
):
    # Embed bauen
    embed = discord.Embed(
        title=f"Einsatzbericht – {planet}",
        description=f"Sektor: **{sektor}**",
        color=discord.Color.red()
    )
    embed.add_field(name="Planet", value=planet, inline=True)
    embed.add_field(name="Sektor", value=sektor, inline=True)
    embed.add_field(name="Feinde", value=gegner, inline=True)
    embed.add_field(name="Mission", value=mission, inline=True)
    embed.add_field(name="Stratagems", value=stratagems, inline=False)
    embed.add_field(name="Helldiver", value=str(helldiver), inline=True)
    embed.add_field(name="Verluste", value=str(verluste), inline=True)
    embed.add_field(name="Ausgang", value=ausgang, inline=True)
    embed.add_field(name="Dauer", value=dauer, inline=True)
    embed.set_footer(text=f"Bericht eingereicht von {ctx.author.display_name}")

    # Beispiel-Bild (kannst später für Planeten ändern)
    embed.set_image(url="https://i.imgur.com/4M34hi2.png")

    await ctx.respond(embed=embed)

# Bot starten mit Token aus Railway Variables
bot.run(os.getenv("TOKEN"))
