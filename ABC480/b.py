import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    s = [input().strip() for _ in range(n)]
    t = [input().strip() for _ in range(m)]

    vote_num = [0] * n

    for voter in t:
        if voter in s:
            vote_num[s.index(voter)] += 1
            continue

        one_char_diffs = []
        for i, candidate in enumerate(s):
            if len(voter) != len(candidate):
                continue

            diff_count = sum(1 for a, b in zip(voter, candidate) if a != b)
            if diff_count == 1:
                one_char_diffs.append(i)

        if len(one_char_diffs) == 1:
            vote_num[one_char_diffs[0]] += 1

    for num in vote_num:
        print(num)
    
if __name__ == "__main__":
    main()