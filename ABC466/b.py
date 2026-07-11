n, m = map(int, input().split())

max_size = [-1] * m
for _ in range(n):
    c, s = map(int, input().split())
    max_size[c-1] = max(max_size[c-1], s)

print(*max_size)