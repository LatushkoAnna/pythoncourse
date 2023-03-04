import collections
import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)

words = []
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                for word in line.split(' '):
                    words.append(word)

cnt = collections.Counter()
for word in words:
    cnt[word] += 1

print("Most common words:", end=" ")
for pair in cnt.most_common(20):
    print(pair[0], end=", ")
print("\nLeast common words:", end=" ")
for i in range(1, 21):
    print(cnt.most_common()[-i][0], end=", ")
