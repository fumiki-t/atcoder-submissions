import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    q = int(input())

    registered = Counter()
    curent_max_id = 0
    for i in range(q):
        s = input()
        if s in registered:
            print(registered[s])
        else:
            curent_max_id += 1
            registered[s] = curent_max_id
            print(curent_max_id)


if __name__ == "__main__":
    main()