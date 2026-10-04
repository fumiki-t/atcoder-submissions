import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, v = map(int, input().split())
w = list(map(int, input().split()))

happiness_max = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if i+j+k+3 <= v:
                happiness_max = max(happiness_max, w[i] + w[j] + w[k])

print(happiness_max)

