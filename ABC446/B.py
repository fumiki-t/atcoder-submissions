N,M = map(int, input().split())
L = []
X = []
sold = set()
for i in range(N):
    L.append(int(input()))
    X.append(list(map(int, input().split())))


for i in range(N):
    flag = True
    for x in X[i]:
        if x not in sold:
            print(x)
            sold.add(x)
            flag = False
            break
    if flag:
        print(0)
        



