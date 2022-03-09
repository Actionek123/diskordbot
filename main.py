import discord
import time
from datetime import date
from datetime import datetime
from discord.ext import commands

token = 'OTM4NDkyMTEzNjE4ODc0NDA5.YfrE5A.tAExEtyfpuHPbwIZuU9PWHswEtc'
bot = commands.Bot(command_prefix='!')


# current_time = now.strftime("%H:%M:%S")

@bot.event
async def on_ready():
    print("Bot is online")


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user:
        return

    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    msg = (f'\n{d1} | {current_time}\n'
           f'    {message.author} napisał\n'
           f'    {message.content}\n')

    f = open("logger.txt", "a")
    f.write(msg)
    f.close()

    if message.content.lower() == "hello":
        await message.channel.send("Hello")

    if message.content.lower() == "bye":
        await message.channel.send("Bye")

    if message.content.lower() == "what is your name?":
        await message.channel.send("Czekaj myślę XD...")
        time.sleep(2)
        await message.channel.send("My name is " + bot.user.name)
    if message.content.lower() == "cool":
        await message.add_reaction('\U0001F60E')


@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


@bot.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )

    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%d/%m/%Y")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    msg = (f'\n{d1} | {current_time}\n'
           f'    {before.author} edit a message.\n'
           f'    Before: {before.content}\n'
           f'    After: {after.content}')

    print(msg)

    f = open("logger.txt", "a")
    f.write(msg)
    f.close()

    # # open and read the file after the appending:
    # f = open("demofile2.txt", "r")
    # print(f.read())


@bot.command()
async def poke(ctx, arg):
    """
        !poke Ania
    """
    await ctx.send(f'Poked {arg}')


@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount + 1)


@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)