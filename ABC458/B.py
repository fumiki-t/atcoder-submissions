h, w = map(int, input().split())

for i in range(h):
    adj_cells = []
    for j in range(w):
        num_cells = 0

        if i-1 >= 0:
            num_cells += 1
        if i+1 < h:
            num_cells += 1
        if j-1 >= 0:
            num_cells += 1
        if j+1 < w:
            num_cells += 1
        adj_cells.append(num_cells)

    print(*adj_cells)