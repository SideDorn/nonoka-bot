import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json
from spell_list_helper import make_spell_embed
from item_name_formatter import format
from wild_magic_helper import wild_magic_embed

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
#gives perms to bot
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
bot = commands.Bot(command_prefix="n!", intents=intents)

with open("spells.json", 'r', encoding="utf-8") as f:
    spell_list = json.load(f)


 #(internal, doesn't affect the actual json) converts the spell name to all lower case

@bot.command()
async def spell(ctx: commands.Context, *args):
    
    spell_name = " ".join(args)
    spell_name = format(spell_name)

    
    try:
        spell_key = spell_list[spell_name] #gets element that corresponds to the name of the spell
        spell_embed = make_spell_embed(spell_key, spell_name)
        await ctx.send(embed = spell_embed)
    except:
        await ctx.send("i don't know this spell... can you teach me?")

@bot.command()
async def wm(ctx: commands.Context, *args):

    numbers = []

    for element in args:
        numbers.append(int(element))
    

    try:
        await ctx.send(embed = wild_magic_embed(numbers))
    except:
        await ctx.send("i dont think that's possible")
    
@bot.command()
async def test(ctx: commands.Context, *args):
    await ctx.send(args)

@bot.command()
async def ult(ctx:commands.Context, *args):
    await ctx.send()

bot.run(token)