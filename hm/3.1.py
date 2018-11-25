s = input()
a = input()
b = input()

'''Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa'''

s = input()
t = input()
i = 0
cnt = 0
for _ in range(len(s)):
    if s.find(t,i) != -1:
        i = s.find(t,i) + 1
        cnt += 1
    else:
        break
print(cnt)