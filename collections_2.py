import collections
import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

s = []
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                s.append((action["character"], line))

d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

with open('result_5_1.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=4)
