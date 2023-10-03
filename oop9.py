#!/usr/bin/python3

import sys


# считывание списка строк из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['10 Сара 37 120000', '2 Фаина 29 12000', '3 Иван 19 12000']


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        begin = 0
        final = len(lst_data) + 1
        if 0 < a < final:
            begin = a
        if a <= b < final:
            final = b
        return self.lst_data[begin: final]

    def insert(self, data):
        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))


db = DataBase()
db.insert(lst_in)
print(db.lst_data)