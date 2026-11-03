import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    heap = a[:k]
    heapify(heap)
    print(heap[0])
    for i in range(k, n):
        if a[i] > heap[0]:
            heappop(heap)
            heappush(heap, a[i])
        print(heap[0])
    pass


if __name__ == "__main__":
    main()