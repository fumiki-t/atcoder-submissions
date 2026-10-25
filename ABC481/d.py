import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

input = sys.stdin.readline


def main():

    n, m, s, t = map(int, input().split())

    s -= 1
    t -= 1
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
    for i in range(n):
        graph[i].sort()

    dist = [float("inf")] * n
    dist[s] = 0
    queue = deque()
    queue.append((s, 0))

    while queue:
        current, fuel = queue.popleft()
        if current == t:
            print(fuel)
            return

        if dist[current] < fuel or not graph[current]:
            continue

        # コスト0での移動
        min_next = graph[current][0]
        if dist[current] < dist[min_next]:
            dist[min_next] = dist[current]
            queue.appendleft((min_next, fuel))

        # コスト1での移動
        for next in graph[current][1:]:
            if dist[current] + 1 < dist[next]:
                dist[next] = dist[current] + 1
                queue.append((next, fuel + 1))

    print(-1)

if __name__ == "__main__":
    main()