from nextcord.ext import commands
import nextcord
class Links(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "hustler", description = "This show give you a link to andrew tate school.")
  async def hustlerslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content="Here's andrew tate school, not for pussy btw.\nhttps://www.hustleruniversity.world")

  @nextcord.slash_command(name = "youtube", description = "This show give you a link to andrew tate youtube.")
  async def youtubeslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content="Here's andrew tate youtube, not for pussy btw.\nhttps://www.youtube.com/c/TateSpeech")

  @nextcord.slash_command(name = "instagram", description = "This show give you a link to andrew tate instagram.")
  async def instagramslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content="Here's andrew tate youtube, not for pussy btw.\nhttps://www.instagram.com/cobratate/")

  @nextcord.slash_command(name = "donate", description = "This show the place to donate for supporting the discord bot.")
  async def donateslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content="Here's the creator buy me a coffee, not for pussy btw.\nhttps://www.buymeacoffee.com/notnoemie")

  @nextcord.slash_command(name = "nerd", description = "This show the place to donate for supporting the discord bot.")
  async def nerdslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content="Hello nerd, no one loves you and no one will never love you.\nHere's your fucking code nerd.\n")

def setup(bot):
  bot.add_cog(Links(bot))
