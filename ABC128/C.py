n, m = map(int, input().split())
k, s = [], []
for i in range(m):
    line = list(map(int, input().split()))
    k.append(line[0])
    s.append(line[1:])

p = list(map(int, input().split()))

ans = 0

for i in range(1 << n):
    all_on = True
    for j in range(m):
        on_count = 0
        for switch in s[j]:
            if (i >> (switch - 1)) & 1:
                on_count += 1
        if on_count % 2 != p[j]:
            all_on = False
            break
    if all_on:
        ans += 1

print(ans)