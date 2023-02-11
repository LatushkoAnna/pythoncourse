import csv


with open('new_table2.csv', 'w', encoding='UTF-8') as f1:
    writer = csv.writer(f1)
    with open('stage3_test.csv', 'r', encoding='UTF-8') as f2:
        reader = csv.reader(f2)
        for row in reader:
            if row == ["Id", "Images", "Title", "Description", "Price"]:
                writer.writerow(row)
            elif 10000 < float(row[4]) <= 50000:
                writer.writerow(row)
