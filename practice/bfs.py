import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    start = None
    
    # BFS
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                # Start position
                start = (r, c)
                break
        if start is not None:
            break

    dist = [[-1] * w for _ in range(h)]
    dist[start[0]][start[1]] = 0

    queue = deque([start])
    while queue:
        r, c = queue.popleft()

        if grid[r][c] == 'G':
            print(dist[r][c])
            return
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + dr, c + dc

            if not (0 <= new_r < h and 0 <= new_c < w):
                continue
            if grid[new_r][new_c] == '#':
                continue
            if dist[new_r][new_c] != -1:
                continue

            dist[new_r][new_c] = dist[r][c] + 1
            queue.append((new_r, new_c))

    print(-1)


if __name__ == "__main__":
    main()