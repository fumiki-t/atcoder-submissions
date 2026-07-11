n = int(input())

cnt = 0
right = 2
for left in range(1,n):
    if right <= left:
        right = left + 1
    while right <= n:
        print(f"? {left} {right}", flush=True)

        ans = input()
        if ans == "Yes":
            right += 1
        else:
            break

    cnt += right - left - 1

print(f"! {cnt}", flush=True)
