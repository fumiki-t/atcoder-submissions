import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
n,k = map(int, input().split())
a = list(map(int, input().split()))

sorted_a = sorted(a)

first_diff_index, last_diff_index = -1, -1

for i in range(n):
    if a[i] != sorted_a[i]:
        if first_diff_index == -1:
            first_diff_index = i
        last_diff_index = i

if last_diff_index - first_diff_index + 1 > k:
    print("No")
else:
    print("Yes")