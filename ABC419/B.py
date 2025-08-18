import bisect

Q = int(input())
A = [list(map(int, input().split())) for _ in range(Q)]

list = []
for i in range(Q):
    if A[i][0] == 1:
        bisect.insort(list, A[i][1])
    if A[i][0] == 2:
        print(list.pop(0))