import csv


with open('new_table3.csv', 'w', encoding='UTF-8') as f1:
    fieldnames = ["Id", "Title", "Price"]
    writer = csv.DictWriter(f1, fieldnames=fieldnames)
    writer.writeheader()
    with open('stage3_test.csv', 'r', encoding='UTF-8') as f2:
        reader = csv.DictReader(f2, delimiter=',')
        for row in reader:
            del row["Images"]
            del row["Description"]
            writer.writerow(row)
