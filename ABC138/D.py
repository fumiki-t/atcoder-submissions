n, q = map(int, input().split())
a, b, p, x = [], [], [], []
for i in range(n-1):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
for i in range(q):
    pi, xi = map(int, input().split())
    p.append(pi)
    x.append(xi)

for i in range(q):