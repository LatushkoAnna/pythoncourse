import json


data = []
with open('wikidata_1000.json', 'r', encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

data1 = {}
for line in data:
    if "description" in line:
        data1[line["label"]["value"]] = line["description"]["value"]
    else:
        data1[line["label"]["value"]] = "None"

with open('result_1.json', 'w') as f:
    json.dump(data1, f, ensure_ascii=False, indent=4)
