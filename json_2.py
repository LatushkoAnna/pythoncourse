import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

data1 = []
for act in data["acts"]:
    for scene in act["scenes"]:
        characters = set()
        for action in scene["action"]:
            characters.add(action["character"])
        data1.append(list(characters))

with open('result_2.json', 'w') as f:
    for line in data1:
        f.write(json.dumps(line, ensure_ascii=False, separators=(',', ':')))
        f.write("\n")
