import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

characters = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in characters:
                characters[action["character"]] = 1
            else:
                characters[action["character"]] = characters[action["character"]] + 1

max_lines = 0
char_name = ""
for character in characters:
    if characters[character] >= max_lines:
        max_lines = characters[character]
        char_name = character
print(char_name)
