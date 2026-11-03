import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    for _ in range(q):
        l, r = map(int, input().split())
        left_index = bisect_left(a, l)
        right_index = bisect_right(a, r)
        products_num = right_index - left_index
        products_price = prefix_sum[right_index] - prefix_sum[left_index]
        print(products_num, products_price)


if __name__ == "__main__":
    main()