from nextcord.ext import commands
from asyncio import sleep
from random import randint
from nextcord import Game
import asyncio

status: list = [
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
  "Why aren't you rich?"
]

class online(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def online_event(self):
    print("I'm online")
    list_max = len(status)
    while True:
      asyncio.create_task(self.bot.change_presence(activity=Game(name=status[randint(0, list_max)])))
      await sleep(3600)
      
      

def setup(bot):
  bot.add_cog(online(bot))
