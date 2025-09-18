import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

GUILD_ID = 1418306356716503042
COUNTER_FILE = "bericht_counter.txt"

# Counter laden
def load_counter():
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "r") as f:
            return int(f.read().strip())
    return 0

# Counter speichern
def save_counter(value):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(value))

bericht_counter = load_counter()  # Beim Start laden

@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")

@bot.slash_command(
    name="helldivers_bericht",
    description="Erstelle einen Helldivers Einsatzbericht",
    guild_ids=[GUILD_ID]
)
async def helldivers_bericht(
    ctx,
    planet: discord.Option(str, "Planet?"),
    sektor: discord.Option(str, "Sektor?"),
    gegner: discord.Option(str, "Gegner", choices=["Automaton", "Terminid", "Illuminate"]),
    mission: discord.Option(str, "Missionsziel?"),
    stratagems: discord.Option(str, "Stratagems/Ausrüstung"),
    helldiver: discord.Option(int, "Anzahl Helldiver", choices=[1,2,3,4]),
    verluste: discord.Option(int, "Gefallene", choices=[0,1,2,3,4]),
    ausgang: discord.Option(str, "Ausgang", choices=["Erfolg", "Teil-Erfolg", "Fehlschlag"]),
    dauer: discord.Option(str, "Einsatzdauer (z.B. 45 Minuten)"),
    map_image: discord.Option(discord.Attachment, "Map-Screenshot hochladen", required=False)
):

    global bericht_counter
    bericht_counter += 1
    save_counter(bericht_counter)  # direkt abspeichern

    nummer = f"#{bericht_counter:04d}"  # 0001, 0002, ...

    embed = discord.Embed(
        title=f"Einsatzbericht {nummer}",
        description=f"**Planet:** {planet}\n**Sektor:** {sektor}",
        color=discord.Color.blue()
    )

    # Thumbnail oben rechts (z. B. Banner, Logo)
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/helldivers_gamepedia/images/7/76/Flag_of_Super_Earth.png")
    
    embed.add_field(name="Feinde", value=gegner, inline=True)
    embed.add_field(name="Mission", value=mission, inline=True)
    embed.add_field(name="Stratagems", value=stratagems, inline=False)
    embed.add_field(name="Helldiver", value=str(helldiver), inline=True)
    embed.add_field(name="Verluste", value=str(verluste), inline=True)
    embed.add_field(name="Ausgang", value=ausgang, inline=True)
    embed.add_field(name="Dauer", value=dauer, inline=True)

    # Großes Bild unten (Map-Screenshot oder Standardbild)
if map_image:
    embed.set_image(url=map_image.url)
else:
    embed.set_image(url="https://helldivers.wiki.gg/images/Ministry_of_Defense_Icon.png")


    embed.set_footer(text=f"Bericht eingereicht von {ctx.author.display_name}")

    await ctx.respond(embed=embed)

bot.run(os.getenv("TOKEN"))
