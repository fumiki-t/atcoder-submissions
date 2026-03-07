def func(n):
    s = str(n)
    rev = s[::-1]
    return int(rev)

x, y = input().split()

a = [int(x), int(y)]
for i in range(8):
    a.append(func(a[i]+a[i+1]))

print(a[9])