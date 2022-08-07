from nextcord.ext import commands
class Censor(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_message")
  async def censor(self, message):
    if any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in message.author.guild_permissions if p[1]])).lower() for word in ['admin']): return
    if any(word in message.content.lower() for word in ['discord.gg/', 'https://']):
      await message.delete()
      await message.channel.send(f'Oh no you cannot post your stupid link for advertising your dumb server, fucking pussy get a life nerd {message.author.mention}.')

def setup(bot):
  bot.add_cog(Censor(bot))
