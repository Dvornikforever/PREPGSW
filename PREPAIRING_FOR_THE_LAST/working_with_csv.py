import csv

amount = 1000

with open("wares.csv", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    lists_of_rows = sorted(reader, key=lambda x: int(x[1]))  # сортировка по цене
    print(lists_of_rows)
