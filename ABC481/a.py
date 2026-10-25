import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    a, b = map(int, input().split())
    sum_digits = len(str(a + b))
    print(sum_digits)


if __name__ == "__main__":
    main()