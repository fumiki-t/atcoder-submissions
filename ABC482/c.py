import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    h, w, n, q = map(int, input().split())

    rows, cols = [], []
    for _ in range(n):
        r, c = map(int, input().split())
        rows.append(r)
        cols.append(c)

    rows.sort()
    cols.sort()

    for _ in range(q):
        num, a, b = map(int, input().split())
        if num == 1:
            count_pieces = bisect_right(rows, b) - bisect_left(rows, a)
            print(count_pieces)
        else:
            count_pieces = bisect_right(cols, b) - bisect_left(cols, a)
            print(count_pieces)
            

if __name__ == "__main__":
    main()