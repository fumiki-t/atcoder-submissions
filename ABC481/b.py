import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    k_count = 0
    for i in range(n-1):
        if a[i] == k:
            k_count += 1
        elif a[i] < k and a[i+1] > k:
            k_count += 1
        elif a[i] > k and a[i+1] < k:
            k_count += 1

    if a[-1] == k:
        k_count += 1
    print(k_count)



if __name__ == "__main__":
    main()