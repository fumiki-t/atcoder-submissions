a, b, c, x, y = map(int, input().split())

min_cost = float('inf')
for i in range(max(x, y) + 1):
    cost = 2 * i * c + max(0, x - i) * a + max(0, y - i) * b
    min_cost = min(min_cost, cost)    

print(min_cost)