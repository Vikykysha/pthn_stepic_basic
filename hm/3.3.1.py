import sys
import re

'''
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.'''


pattern = r".*(cat).*(cat)+"
for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)