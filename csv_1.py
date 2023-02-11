import csv


with open('new_table.csv', 'w', encoding='UTF-8') as f1:
    fieldnames = ["Id", "Images", "Title", "Description", "Price"]
    writer = csv.DictWriter(f1, fieldnames=fieldnames)
    writer.writeheader()
    with open('stage3_test.csv', 'r', encoding='UTF-8') as f2:
        reader = csv.DictReader(f2, delimiter=',')
        for row in reader:
            if len(row["Images"].split(',')) > 3:
                writer.writerow(row)
