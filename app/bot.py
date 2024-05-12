import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
TOKEN = "MTIzODczODY2NzU5ODc3NDMxNA.GAQXT3.rViAosg8KuSN90vtPlfZWAoNhZoYxQvykRC58o"

@client.event
async def on_ready():
    print("봇이 준비되었습니다.")

@client.command(name="ping")
async def get_ping(ctx):
    ping_address = f"@{ctx.author.name}"
    latency = round(client.latency * 1000, 3)  # 응답 시간을 밀리초 단위로 가져와서 3자리까지 잘라줍니다.
    await ctx.send(f'현재 봇의 응답 속도는 {latency}ms 입니다.')
    
client.run(TOKEN)
