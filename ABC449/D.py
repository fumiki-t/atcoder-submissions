l, r, d, u = map(int, input().split())

if l % 2 ==0:
    left = l
else:
    left = l + 1
if r % 2 == 0:
    right = r
else:
    right = r - 1
if d % 2 == 0:
    down = d
else:
    down = d + 1
if u % 2 == 0:
    up = u
else:
    up = u - 1

ans = 0
for i in range(min(left, down), max(right, up)+1, 2):
    if left <= i <= right:
        ans += i - down + 1
    if down <= i <= up:
        ans += i - left 

print(ans)