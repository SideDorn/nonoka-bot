import discord
from discord.ext import commands

def get_ult_details(ult):

    name = ult["name"]
    level = ult["level"]
    description = ult["description"]
    ult_range = ult["range"]
    casting_time = ult["casting_time"]
    charges = ult["charges"]
    


    return name, level, description, ult_range, casting_time, charges

def make_ult_embed(ult):
    name, level, ult_description, ult_range, casting_time, charges = get_ult_details(ult)


    embed = discord.Embed(title=f'Details for Level {level}: **{name}**', description=ult_description)

    embed.add_field(name = "Range", value = ult_range)
    embed.add_field(name = "Casting Time", value = casting_time)
    embed.add_field(name = "Charges/LR", value = charges)
    embed.add_field(name = "Casting Time", value = casting_time)




    
    return embed
