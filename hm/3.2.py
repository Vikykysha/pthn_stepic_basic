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