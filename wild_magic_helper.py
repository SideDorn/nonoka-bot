import json
import math
import discord

with open("wild_magic_table.json", 'r', encoding="utf-8") as f:
    wild_magic_table = json.load(f)

def wild_magic(number):
    if number > 0:
        return wild_magic_table[math.ceil(number/2) - 1]
    else: return wild_magic_table[200]

def wild_magic_embed(numbers):
    effect = wild_magic(numbers[0])
    embed = discord.Embed(title = f"Your wild magic surge rolled **{numbers[0]}**!", description=effect)

    other_rolls = ""
    i = 1
    while i < len(numbers):

        other_rolls += f"{numbers[i]} - {wild_magic(numbers[i])} \n"
        print(other_rolls)
        
        

        i += 1
        
    embed.add_field(name = "Other Rolls", value = other_rolls)
    return embed
