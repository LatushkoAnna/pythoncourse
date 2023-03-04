import collections
import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

cnt = collections.Counter()
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                cnt[action["character"]] += 1
print(cnt)
