import re
import sys

'''Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.'''

pattern = r"human"
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern,"computer",line))