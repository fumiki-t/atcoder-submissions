import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():
    if input().strip()[0] in ["A", "D"]:
        if input().strip()[1] in ["A", "D"]:
            print("No")
        else:
            print("Yes")
    else:
        if input().strip()[1] in ["A", "D"]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()