s = input()

cnt = 0

for i in range(len(s)):
    if s[i] == 'C':
        cnt += min(i+1, len(s)-i)

print(cnt)