import json
from ult_helper import get_ult_details
with open("ults.json", 'r', encoding="utf-8") as f:
    ults = json.load(f)

character_name = "Anne Marie Yuu"
character_ults = ults[character_name]

for element in character_ults:
    if element["name"] != "":
        print(get_ult_details(element))
        

