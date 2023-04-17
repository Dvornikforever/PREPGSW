import csv

with open('plantis.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for dct in reader:
        print(dct['nomen'])
