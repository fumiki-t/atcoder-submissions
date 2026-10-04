import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n, q = map(int, input().split())

sets = [[] for _ in range(n+1)]
for _ in range(q):
    l, r, x = map(int, input().split())
    sets[l-1].append((x, 1))
    sets[r].append((x, -1))

set_size = [0] * n

counter = defaultdict(int)
unique_count = 0

for i in range(n):
    for x, delta in sets[i]:
        if counter[x] == 0 and delta ==1:
            unique_count += 1
        counter[x] += delta
        if counter[x] == 0 and delta == -1:
            unique_count -= 1

    set_size[i] = unique_count

print(*set_size)