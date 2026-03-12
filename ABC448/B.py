n, m = map(int, input().split())
c = list(map(int, input().split())) #pepper総量
a, b = [], [] 
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai) # aiはpepper番号
    b.append(bi) # biはpepper使用量

pepper_sum = 0
for i in range(n):
    if c[a[i]-1] >= b[i]:
        pepper_sum += b[i]
        c[a[i]-1] -= b[i]
    elif c[a[i]-1] > 0:
        pepper_sum += c[a[i]-1]
        c[a[i]-1] = 0

print(pepper_sum)
