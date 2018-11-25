import sys
import re
'''Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).'''
pattern = r"\b(.+)\1\b"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)