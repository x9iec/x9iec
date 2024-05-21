import discord
from discord.ext import commands

client = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
token = 'MTI0MjQyOTYxNzIyNzMwMDkzNA.G1g2Yc.YFRZ52x_36WBdRxCAKzcWdsDuujSjDUV-6HDeY'

@client.event
async def on_ready():
    await client.tree.sync()

@client.command(name="청소")
async def clear(ctx, amount: int):
    try:
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount}개의 메시지가 삭제되었습니다.")
    except ValueError:
        await ctx.send("숫자로 된 수량을 입력하세요.")

client.run(token)
