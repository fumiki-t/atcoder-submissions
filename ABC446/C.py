from collections import deque

T = int(input())
N,D,A,B = [],[],[],[]
for i in range(T):
    n,d = map(int, input().split())
    N.append(n)
    D.append(d)
    A.append(list(map(int, input().split())))
    B.append(list(map(int, input().split())))

for i in range(T):
    k = 0
    for j in range(N[i]):

        while B[i][j] > 0:
            if A[i][k] >= B[i][j]:
                A[i][k] -= B[i][j]
                B[i][j] = 0
            else:
                B[i][j] -= A[i][k]
                A[i][k] = 0
                k+=1
        
        if j >= D[i]:
            A[i][j-D[i]] = 0
    print(sum(A[i]))
