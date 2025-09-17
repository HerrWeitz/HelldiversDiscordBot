import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

GUILD_ID = 1415795711747817545

@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")

@bot.slash_command(
    name="helldivers_bericht",
    description="Erstelle einen Helldivers Einsatzbericht",
    guild_ids=[GUILD_ID]  # <--- sorgt dafür, dass es sofort da ist
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
    dauer: discord.Option(str, "Einsatzdauer (45 Minuten)")
    map_image: discord.Option(discord.Attachment, "Map-Screenshot hochladen") = None

):
    embed = discord.Embed(
        title=f"Einsatzbericht – {planet}",
        description=f"Sektor: **{sektor}**",
        color=discord.Color.from_rgb(0, 102, 204)  # schönes Blau
    )
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/helldivers_gamepedia/images/7/76/Flag_of_Super_Earth.png/revision/latest/scale-to-width-down/1200?cb=20250207171045")  # Beispiel-Logo/Banner
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

    embed.set_image(url="https://helldivers.wiki.gg/images/Ministry_of_Defense_Icon.png?a8a8a0")
    if map_image:
        embed.set_image(url=map_image.url)

    await ctx.respond(embed=embed)

bot.run(os.getenv("TOKEN"))
