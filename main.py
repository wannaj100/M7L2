import discord
from discord.ext import commands
from model import get_class
import os, random
import requests
from PIL import Image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    
    await before.channel.send("treść wiadomości przed edycją: " + before.content)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def password(ctx, count_gen = 8):
    await ctx.send(password(count_gen))
    
@bot.command()
async def suma(ctx, *numbers):
    liczby = []
    for number in numbers:
        liczby.append(int(number))
    await ctx.send(sum(liczby))
        
@bot.command()
async def repeat(ctx, count_heh = 5, linia="", content='', a = "" , s = "" , d = "",f = "",g = "",h = ""):
    if linia == "pionowo":
        await ctx.send((content +" "+ a +" "+ s +" "+ d +" "+ f+" "+ g+" "+ h+ "\n") * count_heh)
    elif linia == "poziomo":
        await ctx.send((content +" "+ a +" "+ s +" "+ d +" "+ f+" "+ g+" "+ h+ "") * count_heh)
    else:
        await ctx.send("Nie poprawna: komenda, kolejność bądź kierunek tekstu")
    
@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            name = attachment.filename
            await attachment.save(f'./{name}')
            image = Image.open(file_name)
            await ctx.send(get_class(image, 'keras_model.h5', "labels.txt"))
    else:
        await ctx.send("Nie przesłałeś żadnego piku")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
