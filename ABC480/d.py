import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    # aの累積和：prefix_a[i] = a[0] + a[1] + ... + a[i-1]
    prefix_a = [0] * (n + 1)
    # bの各群の終了位置を記録する配列
    ends = [0] * (n + 1)
    # bの累積和：prefix_b[i] = a[0] + (a[0] + a[1]) + ... + (a[0] + a[1] + ... + a[i-1]) = prefix_a[1] + prefix_a[2] + ... + prefix_a[i]
    prefix_b = [0] * (n + 1)

    for i in range(n):
        prefix_a[i+1] = prefix_a[i] + a[i] 
        ends[i+1] = (i + 1) * (i + 2) // 2
        prefix_b[i+1] = prefix_b[i] + prefix_a[i+1]

    def f(x):
        j = bisect_right(ends, x) - 1
        remaining = x - ends[j]
        return prefix_b[j] + prefix_a[remaining]

    for l, r in queries:
        print(f(r) - f(l-1))

if __name__ == "__main__":
    main()