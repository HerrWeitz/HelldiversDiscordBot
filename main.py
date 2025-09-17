import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

# Sync Slash-Commands bei Start
@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"🔧 {len(synced)} Slash-Commands synchronisiert")
    except Exception as e:
        print(f"Fehler beim Sync: {e}")

# Slash Command: Helldivers Bericht
@bot.tree.command(name="helldivers_bericht", description="Erstelle einen Helldivers Einsatzbericht")
@app_commands.describe(
    planet="Welcher Planet?",
    sektor="Welcher Sektor?",
    gegner="Gegnerfraktion",
    mission="Missionsziel",
    stratagems="Verwendete Stratagems / Ausrüstung",
    helldiver="Anzahl der Helldiver (1–4)",
    verluste="Gefallene Helldiver",
    ausgang="Missionsergebnis",
    dauer="Einsatzdauer"
)
@app_commands.choices(
    gegner=[
        app_commands.Choice(name="Automaton", value="Automaton"),
        app_commands.Choice(name="Terminid", value="Terminid"),
        app_commands.Choice(name="Illuminate", value="Illuminate")
    ],
    helldiver=[
        app_commands.Choice(name="1", value=1),
        app_commands.Choice(name="2", value=2),
        app_commands.Choice(name="3", value=3),
        app_commands.Choice(name="4", value=4)
    ],
    verluste=[
        app_commands.Choice(name="0", value=0),
        app_commands.Choice(name="1", value=1),
        app_commands.Choice(name="2", value=2),
        app_commands.Choice(name="3", value=3),
        app_commands.Choice(name="4", value=4)
    ],
    ausgang=[
        app_commands.Choice(name="Erfolg", value="Erfolg"),
        app_commands.Choice(name="Teil-Erfolg", value="Teil-Erfolg"),
        app_commands.Choice(name="Fehlschlag", value="Fehlschlag")
    ]
)
async def helldivers_bericht(
    interaction: discord.Interaction,
    planet: str,
    sektor: str,
    gegner: app_commands.Choice[str],
    mission: str,
    stratagems: str,
    helldiver: app_commands.Choice[int],
    verluste: app_commands.Choice[int],
    ausgang: app_commands.Choice[str],
    dauer: str
):
    embed = discord.Embed(
        title=f"Einsatzbericht – {planet}",
        description=f"Sektor: **{sektor}**",
        color=discord.Color.red()
    )
    embed.add_field(name="Gegner", value=gegner.value, inline=True)
    embed.add_field(name="Mission", value=mission, inline=True)
    embed.add_field(name="Stratagems", value=stratagems, inline=False)
    embed.add_field(name="Helldiver", value=str(helldiver.value), inline=True)
    embed.add_field(name="Verluste", value=str(verluste.value), inline=True)
    embed.add_field(name="Ausgang", value=ausgang.value, inline=True)
    embed.add_field(name="Dauer", value=dauer, inline=True)

    embed.set_footer(text=f"Bericht eingereicht von {interaction.user.display_name}")
    embed.set_thumbnail(url="https://i.imgur.com/QpZkZ4h.png")  # kleines Bild
    embed.set_image(url="https://i.imgur.com/4M34hi2.png")      # großes Banner

    await interaction.response.send_message(embed=embed)

# Bot starten
bot.run(os.getenv("TOKEN"))
