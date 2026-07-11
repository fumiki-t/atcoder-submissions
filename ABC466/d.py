n, m = map(int, input().split())

rooks_positions = []
for _ in range(m):
    r, c = map(int, input().split())
    rooks_positions.append((r, c))


cnt = 0
removed_rows = set()
removed_cols = set()
for r, c in reversed(rooks_positions):
    if r not in removed_rows and c not in removed_cols:
        cnt += 1
    removed_rows.add(r)
    removed_cols.add(c)

print(cnt)