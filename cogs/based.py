from nextcord.ext import commands
import nextcord
from random import randint
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

def setup(bot):
  bot.add_cog(Funny(bot))
