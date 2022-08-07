from nextcord.ext import commands
import nextcord
from random import randint
import requests
from json import loads
from os import environ
funfact: list = [
  "Getting rich from other people",
  'What colour is your bugatti?',
  'You had a heart attack? get tf up',
  'BREATH AIR!',
  'Do some push ups',
  'with a brokie!',
  'Are you scared of bubbles?',
  "Smoking a cigar",
  "Heart attacks are for pussy.",
  "Are you dumb?",
  "Why aren't you rich?",
  "Depression is for pussy."
]
class Funny(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "based", description = "This command will give you some based sentences.")
  async def basedslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content=funfact[randint(0, len(funfact))])

  @nextcord.slash_command(name = "image", description = "This command will give you some random image of something.")
  async def imageslash(self, interaction: nextcord.Interaction, theme: str = nextcord.SlashOption(name="theme", description="The theme for your stupid research.")):
    if theme.lower() in ['andrew', 'tate']: return await interaction.response.send_message(content="My photos are not gonna show in a fucking dumb bot, are you retarted?")
    r = requests.get(f'https://api.pexels.com/v1/search?query={theme}', headers={"Authorization": environ['pexel']})
    content = loads(r.content.decode('utf-8'))
    try:
      await interaction.response.send_message(embed=nextcord.Embed(title=f"Dumb photo of {theme}.", color=0x3498db).set_image(content['photos'][randint(0, len(content['photos']))]['src']['original']))
    except:
      await interaction.response.send_message(f"This stupid api tool cannot find a fucking image of {theme}")

def setup(bot):
  bot.add_cog(Funny(bot))
