import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))

balls_with_idx = [(a[i], i+1) for i in range(n)]
small_6 = sorted(balls_with_idx)[:6]

k, b = [], []
for i in range(q):
    ki = int(input())
    bi = list(map(int, input().split()))
    k.append(ki)
    b.append(bi)

for i in range(q):
    for num, idx in small_6:
        if idx not in b[i]:
            print(num)
            break