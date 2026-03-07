import numpy as np

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(k)]

ans = np.zeros((n, m))

for i in range(k):
    ans[A[i][0]-1, A[i][1]-1] = 1
    if np.all(ans[A[i][0]-1] == 1):
        print(A[i][0], end=" ")