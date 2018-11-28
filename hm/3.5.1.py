import csv
'''Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.'''
with open('Crimes','r') as f:
    reader = csv.DictReader()
    d = {}
    for row in reader:
        if 'CHICAGO' in row['Block'] and '2015' in row['Date']:
            d[row['Primary Type']] = d.get(row['Primary Type'],0) + 1
    print(max(d,key = d.get))
