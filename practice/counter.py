import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    counter = Counter(a[:k])
    max_numbers = len(counter)

    for i in range(n-k):
        counter[a[i]] -= 1
        if counter[a[i]] == 0:
            del counter[a[i]]
        counter[a[i+k]] += 1
        max_numbers = max(max_numbers, len(counter))

    print(max_numbers)

if __name__ == "__main__":
    main()