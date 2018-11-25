'''Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.'''
import sys
import re

pattern = r"(z...z)"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)
