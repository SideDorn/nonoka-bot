import discord
from discord.ext import commands

def get_spell_details(spell):
    casting_time = spell["casting_time"]
    components = spell["components"]
    description = spell["description"]
    duration = spell["duration"]
    level = spell["level"]
    spell_range = spell["range"]
    school = spell["school"]


    return casting_time, components, description, duration, level, spell_range, school

def make_spell_embed(spell, spell_name):
    casting_time, components, spell_description, duration, level, spell_range, school = get_spell_details(spell)


    embed = discord.Embed(title=f'Details for **{spell_name}**', description=spell_description)

    embed.add_field(name = "Casting Time", value = casting_time)
    embed.add_field(name = "Components", value = components)
    embed.add_field(name = "Duration", value = duration)
    embed.add_field(name = "Level", value = level)
    embed.add_field(name = "Range", value = spell_range)
    embed.add_field(name = "School", value = school)

    
    return embed
