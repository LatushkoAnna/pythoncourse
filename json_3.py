import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

characters = []
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in characters:
                characters.append(action["character"])
data1 = {}
for character in characters:
    count = 0
    for act in data["acts"]:
        for scene in act["scenes"]:
            for action in scene["action"]:
                if action["character"] == character:
                    count += 1
    data1[character] = count

max_lines = 0
char_name = None
for character in data1:
    if data1[character] >= max_lines:
        max_lines = data1[character]
        char_name = character
print(char_name)
