from itertools import combinations

n = int(input())
s = input()

ans = 0
for i in range(1000):
    target = f"{i:03d}"

    idx0 = s.find(target[0])
    if idx0 == -1:
        continue

    idx1 = s.find(target[1], idx0 + 1)
    if idx1 == -1:
        continue

    idx2 = s.find(target[2], idx1 + 1)
    if idx2 != -1:
        ans += 1

print(ans)