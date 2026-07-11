n = int(input())
x = list(map(int, input().split()))

for happiness in x:
    if happiness >= 0:
        print("No")
        break
else:
    print("Yes")