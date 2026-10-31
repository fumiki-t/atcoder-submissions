import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    n = int(input())
    x = list(map(int, input().split()))

    for k in range(1, n + 1):
        if k == 1:
            time = (x[-1] - x[0]) // 2
        elif k == n:
            time = (x[-1] - x[0]) // 2
        else:
            time_to_right = max((x[k] - x[0]) // 2, (x[-1] - x[k - 1]) // 2)
            time_to_left = max((x[k - 1] - x[0]) // 2, (x[-1] - x[k - 2]) // 2)
            time = min(time_to_right, time_to_left)
        print(int(time))



if __name__ == "__main__":
    main()