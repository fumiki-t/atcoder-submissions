import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    grid = [list(input().strip()) for _ in range(5)]
    min_bingo = 5

    # 横のビンゴ
    for i in range(5):
        o_count = 0
        for j in range(5):
            if grid[i][j] == "o":
                o_count += 1
        min_bingo = min(min_bingo, 5 - o_count)

    # 縦のビンゴ
    for j in range(5):
        o_count = 0
        for i in range(5):
            if grid[i][j] == "o":
                o_count += 1
        min_bingo = min(min_bingo, 5 - o_count)

    # 斜めのビンゴ
    o_count_rd = 0
    o_count_ru = 0
    for k in range(5):
        if grid[k][k] == "o":
            o_count_rd += 1
    min_bingo = min(min_bingo, 5 - o_count_rd)

    for l in range(5):
        if grid[l][4-l] == "o":
            o_count_ru += 1
    min_bingo = min(min_bingo, 5 - o_count_ru)

    print(min_bingo)
    


if __name__ == "__main__":
    main()