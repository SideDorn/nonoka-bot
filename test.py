import json
import re
from ult_helper import get_ult_details
with open("ults.json", 'r', encoding="utf-8") as f:
    ults = json.load(f)

character_name = "Ann"
test = r"[\w\W]*" + character_name + r"[\w\W]*"
test = (re.compile(test))
newlist = list(filter(test.match, ults))
character_name = newlist[0]
print(newlist)
character_ults = ults[character_name]

for element in character_ults:
    if element["name"] != "":
        print(get_ult_details(element))
        

