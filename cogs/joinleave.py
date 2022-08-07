from nextcord.ext import commands
import nextcord
from nextcord.abc import GuildChannel
from internaldb import add, get_one
class Joinleave(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_member_join")
  async def join(self, member):
    await self.bot.get_channel(get_one(member.guild.id, 'joinleave')['join']).send(embed=nextcord.Embed(title=f"Welcome to the server {member.name}", description="I hope you are not a pussy.", color=0x2ecc71).set_image(member.avatar.url))

  @nextcord.slash_command(name = "join", description = "This command is for the setup of the join and leave utils.")
  async def joinslash(self, interaction: nextcord.Interaction, channel: GuildChannel = nextcord.SlashOption(name="channel", description="The join channel", channel_types=[nextcord.ChannelType.text])):
    if not any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in interaction.user.guild_permissions if p[1]])).lower() for word in ['admin']): return await interaction.response.send_message(content=f"You need admin to setup this fucking retard.", ephemeral=True)
    add(interaction.guild.id, {"join": channel.id}, 'joinleave')
    await channel.send(embed=nextcord.Embed(title="This channel is the new channel when the user joins.", color=0xe74c3c).set_image('https://media.tenor.com/images/93ad4135631b54f78e0473f1d10baa13/tenor.gif'))
    await interaction.response.send_message(content=f"Join setup for the channel {channel.mention} was succesfull.", ephemeral=True)

  @commands.Cog.listener("on_member_remove")
  async def leave(self, member):
    await self.bot.get_channel(get_one(member.guild.id, 'joinleave')['leave']).send(embed=nextcord.Embed(title=f"Bye {member.name}", description="If you join my server and you fucking leave, you are a pussy, so you don't deserve to leave.", color=0x2ecc71).set_image(member.avatar.url))

  @nextcord.slash_command(name = "leave", description = "This command is for the setup of the join and leave utils.")
  async def leaveslash(self, interaction: nextcord.Interaction, channel: GuildChannel = nextcord.SlashOption(name="channel", description="The leave channel", channel_types=[nextcord.ChannelType.text])):
    if not any(word in str(', '.join([str(p[0]).replace("_", " ").title() for p in interaction.user.guild_permissions if p[1]])).lower() for word in ['admin']): return await interaction.response.send_message(content=f"You need admin to setup this fucking retard.", ephemeral=True)
    add(interaction.guild.id, {"leave": channel.id}, 'joinleave')
    await channel.send(embed=nextcord.Embed(title="This channel is the new channel when the user leave.", color=0xe74c3c).set_image('https://media.tenor.com/images/93ad4135631b54f78e0473f1d10baa13/tenor.gif'))
    await interaction.response.send_message(content=f"Leave setup for the channel {channel.mention} was succesfull.", ephemeral=True)

def setup(bot):
  bot.add_cog(Joinleave(bot))
