import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    s = input().strip()
    o_count = 0
    for a in s:
        if a == "o":
            o_count += 1

    if o_count % 2 == 0:
        print("even")
    else:
        print("odd")



if __name__ == "__main__":
    main()