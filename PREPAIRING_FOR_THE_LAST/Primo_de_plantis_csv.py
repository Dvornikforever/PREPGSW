import csv
from sys import stdin

list_of_terms = ['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia']
total_list_of_dicts = []
for line in stdin:
    dct = {}
    for i, word in enumerate(line.rstrip('\n').split('\t')):
        dct[list_of_terms[i]] = word
    total_list_of_dicts.append(dct)

with open('plantis.csv', encoding='utf-8', newline='', mode='w') as csvfile:
    writer = csv.DictWriter(
        csvfile, fieldnames=list(total_list_of_dicts[0].keys()),
        delimiter=';', quoting=csv.QUOTE_NONE)
    writer.writeheader()
    for dct in total_list_of_dicts:
        writer.writerow(dct)
