import sys
import re

'''Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".'''

pattern = r"\\"
for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(line)
