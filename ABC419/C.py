N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

rows = [a[0] for a in A]
columns = [a[1] for a in A]

width = max(rows) - min(rows)
height = max(columns) - min(columns)

ans = max((width + 1)//2, (height + 1)//2)
print(ans)