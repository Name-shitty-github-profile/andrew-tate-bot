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

  @nextcord.slash_command(name = "nerd", description = "This show the source code of the bot, for the nerds.")
  async def nerdslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(content="Hello nerd, no one loves you and no one will never love you.\nHere's your fucking code nerd.\nhttps://github.com/Name-shitty-github-profile/andrew-tate-bot")

  @nextcord.slash_command(name = "addme", description = "This show a link to add me.")
  async def addmeslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message(embed=nextcord.Embed(title="Add me", description="[Click here to add me](https://discord.com/api/oauth2/authorize?client_id=1005589411259486259&permissions=8&scope=bot%20applications.commands)\nCan't click?\nHere's another way to add me : https://discordbotlist.com/bots/andrew-tate", color = 0x2ecc71))

def setup(bot):
  bot.add_cog(Links(bot))
