from nextcord.ext import commands
import nextcord
from random import randint
funhelp: list = [
  "Can't you fucking read?",
  "I'm usefull, suggest some shit to my creator, fucking nerd",
  "Are you dumb?",
  "You are probably poor.",
  "Sounds like someone that doesn't get any bitches."
]
class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "image", description = "The help of the bot.")
  async def helpslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content=funhelp[randint(0, len(funhelp))])

def setup(bot):
  bot.add_cog(Help(bot))
