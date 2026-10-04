import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())

greap_num = [0] * n
distributed_greaps = m // n
remaining_greaps = m % n

for i in range(n):
    greap_num[i] = distributed_greaps
    if i < remaining_greaps:
        greap_num[i] += 1
    print(greap_num[i])

