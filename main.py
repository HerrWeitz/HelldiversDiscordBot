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
        title=f"Einsatzbericht",
        description=f"**Planet:** {planet}\n**Sektor:** {sektor}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Feinde", value=gegner, inline=True)
    embed.add_field(name="Mission", value=mission, inline=True)
    embed.add_field(name="Stratagems", value=stratagems, inline=False)
    embed.add_field(name="Helldiver", value=str(helldiver), inline=True)
    embed.add_field(name="Verluste", value=str(verluste), inline=True)
    embed.add_field(name="Ausgang", value=ausgang, inline=True)
    embed.add_field(name="Dauer", value=dauer, inline=True)

    # Thumbnail oben rechts
    embed.set_thumbnail(url="https://static.wikia.nocookie.net/helldivers_gamepedia/images/7/76/Flag_of_Super_Earth.png")

    # Map-Bild unten
    if map_image:
        embed.set_image(url=map_image.url)
    else:
        embed.set_image(url="https://helldivers.wiki.gg/images/Ministry_of_Defense_Icon.png")

    embed.set_footer(text=f"Bericht eingereicht von {ctx.author.display_name}")

    # ✅ Wichtig: await bleibt DRIN in der Funktion
    await ctx.respond(embed=embed)
