import discord
from discord.ext import commands
from discord.ext import pages
import os
from dotenv import load_dotenv
import json
from spell_list_helper import make_spell_embed
from item_name_formatter import format
from wild_magic_helper import wild_magic_embed
from ult_helper import make_ult_embed, get_ult_details

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
with open("ults.json", 'r', encoding="utf-8") as f:
    ult_list = json.load(f)
#reading all of the json files before bot starts up


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
async def ults(ctx:commands.Context, *args):

    character_name = format(" ".join(args))

    ult_pages = []


    try:  
        character_ults = ult_list[character_name]
        for element in character_ults:          
            if element["name"] != "":
                print(get_ult_details(element))
                ult_embed = make_ult_embed(element)
                ult_page = discord.ext.pages.Page(content = f"Ults for **{character_name}**", embeds = [ult_embed])
                ult_pages.append(ult_page)  
        # makes each page and adds the ult details
        ult_paginator = discord.ext.pages.Paginator(ult_pages)
        await ult_paginator.send(ctx=ctx)
    except:
        await ctx.send("that isnt a character...")

@bot.command()
async def wm(ctx: commands.Context, *args):

    numbers = []

    for element in args:
        numbers.append(int(element))
    

    try:
        await ctx.send(embed = wild_magic_embed(numbers))
    except:
        await ctx.send("i dont think that's possible")

# content is the message




@bot.command()
async def test(ctx: commands.Context):
    test_page_1 = discord.ext.pages.Page(content = "test", embeds=[discord.Embed(title="test")])
    test_page_2 = discord.ext.pages.Page(content = "skjlfsdf", embeds=[discord.Embed(title="awawaw")])

    test_paginator = discord.ext.pages.Paginator([test_page_1, test_page_2])

    await test_paginator.send(ctx=ctx) 



bot.run(token)