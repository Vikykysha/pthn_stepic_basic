import sys
import re

'''Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".'''

pattern = r"\b[a|A]+\b"

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern,'argh', line, count = 1))