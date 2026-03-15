n, l, r = map(int, input().split())
s = input()

ans = 0
#累積和使えそう
cum_sum = [[0] * 26 for _ in range(n+1)]
for i in range(n):
    for j in range(26):
        cum_sum[i+1][j] = cum_sum[i][j]
    cum_sum[i+1][ord(s[i]) - ord("a")] += 1

for i in range(n):
    ans += cum_sum[min(r+i+1, n)][ord(s[i]) - ord("a")] - cum_sum[min(l+i, n)][ord(s[i]) - ord("a")]

print(ans)