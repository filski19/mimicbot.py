import discord
import nacl
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def set_avatar(ctx, member: discord.Member):
    with open('avatar.png', 'wb') as f:
        await member.avatar.save(f)
    with open('avatar.png', 'rb') as f:
        avatar = f.read()
    await bot.user.edit(avatar=avatar)
    await ctx.send(f"Changed avatar to {member.name}'s avatar")

@bot.command()
async def set_name(ctx, member: discord.Member):
    await bot.user.edit(username=member.name)
    await ctx.send(f"Changed name to {member.name}")

@bot.command()
async def join(ctx, voice_channel_id: int):
    channel = bot.get_channel(voice_channel_id)
    voice = await channel.connect()

# bot.run('Insert Your Bot Token')