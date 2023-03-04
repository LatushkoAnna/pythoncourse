import collections
import csv

with open('result_5_2.csv', 'w', encoding='UTF-8') as f1:
    writer = csv.writer(f1)
    with open('stage3_test.csv', 'r', encoding='UTF-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        d = {}
        for row in reader:
            d[row["Id"]] = float(row["Price"])
        od = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1]))
        for item in od:
            writer.writerow([item, od[item]])
with open('result_5_3.csv', 'w', encoding='UTF-8') as f2:
    writer = csv.writer(f2)
    od1 = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))
    for item in od1:
        writer.writerow([item, od1[item]])
