import collections
import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

d = collections.defaultdict(list)
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                d[action["character"]].append(line)

with open('result_5_1.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
