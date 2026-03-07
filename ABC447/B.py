from collections import Counter

s = input()

c = Counter(s)
max_count = max(c.values())
keys = [k for k, v in c.items() if v == max_count]

ans = "".join(a for a in s if a not in keys)

print(ans)