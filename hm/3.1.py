s = input()
a = input()
b = input()

if a in b:
    print('Impossible')
elif a not in s:
    print('Impossible')
else:
    while a in s:
        cnt = 0
        s.replace(a,b)
        cnt += 1
    print(cnt)
