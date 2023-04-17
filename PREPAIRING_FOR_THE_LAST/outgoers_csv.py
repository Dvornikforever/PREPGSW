import csv

amount_of_percents = int(input())
with open('vps.csv', encoding='utf-8', mode='r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    print('\n'.join([dct['Специальность'] for dct in reader if int(dct['соответствует в %']) >= amount_of_percents]))
