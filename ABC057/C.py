n = int(input())
min_f = float('inf')

for a in range(1, int(n**0.5) + 1):
    if n % a == 0:
        b = n / a
        f = max(len(str(int(a))), len(str(int(b))))

        min_f = min(min_f, f)

print(min_f)