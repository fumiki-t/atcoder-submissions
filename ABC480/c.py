import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

def main():
    n, k, t = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    
    push_sum = 0
    current_end = 0 
    
    for x in a:
        if current_end >= t:
            break
        
        if x > current_end:
            interval = min(x, t) - current_end
            push_sum += (interval + k - 1) // k
        
        current_end = max(current_end, x + k)

    if current_end < t:
        interval = t - current_end
        push_sum += (interval + k - 1) // k

    print(push_sum)

if __name__ == "__main__":
    main()
