h, w, q = map(int, input().split())

for _ in range(q):
    num, x = map(int, input().split())
    if num == 1:
        print(x * w)
        h -= x
    else:
        print(x * h)
        w -= x