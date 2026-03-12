n = int(input())
cnt_8_divisors = 0

for i in range(1, n+1, 2):
    cnt = 0
    for j in range(1, int(i**0.5)+1):
        if i % j == 0:
            if j * j == i:
                cnt += 1
            else:
                cnt += 2
    if cnt == 8:
        cnt_8_divisors += 1

print(cnt_8_divisors)