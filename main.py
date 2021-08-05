from colorama import Fore
import asyncio
import random

import discord
from discord.ext import commands
from datetime import timedelta

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help Autodanker", color=420699, description=f"**{prefix}autodank**\nsends pls beg, pls fish, pls hunt and pls dep all every 50 seconds.\n\n**{prefix}stopautodank**\nstops autodank.")
  await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def autodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **enabled**!')
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			await asyncio.sleep(3)
			await ctx.send('pls fish')
			print(f"{Fore.GREEN}succefully fished")
			await ctx.send('pls se 500')
			print(f"{Fore.GREEN}succefully snake eyed")
			await ctx.send('pls bet 500')
			print(f"{Fore.GREEN}succefully bet")
			await ctx.send('pls hunt')
			print(f"{Fore.GREEN}succefully hunted")
			await asyncio.sleep(47)


@bot.command()
async def stopautodank(ctx):
	await ctx.message.delete()
	await ctx.send('auto dank memer is now **disabled**!')
	global dmcs
	dmcs = False
