import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

data1 = []
for act in data["acts"]:
    for scene in act["scenes"]:
        characters = []
        for action in scene["action"]:
            if action["character"] not in characters:
                characters.append(action["character"])
        data1.append(characters)

with open('result_2.json', 'w') as f:
    f.write(json.dumps(data1, ensure_ascii=False, indent=4))
