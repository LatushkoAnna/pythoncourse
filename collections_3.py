import collections
import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

lines = []
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                lines.append(action["character"])

cnt = collections.Counter()
for line in lines:
    cnt[line] += 1
print(cnt)
