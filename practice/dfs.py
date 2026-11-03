import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    n, k, s = map(int, input().split())
    a = list(map(int, input().split()))

    def dfs(current_count, current_sum, current_index):
        if current_count == k:
            if current_sum == s:
                return True
            else:
                return False
        if current_index >= n:
            return False

        # Include the current element
        if dfs(current_count + 1, current_sum + a[current_index], current_index + 1):
            return True

        # Exclude the current element
        if dfs(current_count, current_sum, current_index + 1):
            return True

        return False


if __name__ == "__main__":
    main()