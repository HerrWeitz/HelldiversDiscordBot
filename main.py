import discord
from discord.ext import commands

# Bot erstellen
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# Event: Bot startet
@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")

# Slash Command Beispiel
@bot.slash_command(
    name="helldivers_bericht",
    description="Erstelle einen Helldivers Einsatzbericht"
)
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
    dauer: discord.Option(str, "Einsatzdauer (z. B. 45 Minuten)"),
    map_image: discord.Option(discord.Attachment, "Map-Screenshot hochladen", required=False)
):
    embed = discord.Embed(
        title=f"Einsatzbericht – {planet}",
        description=f"Sektor: **{sektor}**",
        color=discord.Color.blue()
    )
    embed.add_field(name="Feinde", value=gegner, inline=True)
    embed.add_field(name="Mission", value=mission, inline=True)
    embed.add_field(name="Stratagems", value=stratagems, inline=False)
    embed.add_field(name="Helldiver", value=str(helldiver), inline=True)
    embed.add_field(name="Verluste", value=str(verluste), inline=True)
    embed.add_field(name="Ausgang", value=ausgang, inline=True)
    embed.add_field(name="Dauer", value=dauer, inline=True)

    # Thumbnail (immer gleich)
    embed.set_thumbnail(url="https:_
