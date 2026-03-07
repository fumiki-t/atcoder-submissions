n = int(input())
counter = 0

for i in range(len(str(n))):
    if n%10 == 1:
        counter += 1
    n //= 10

print(counter)
    