from collections import deque
s = input()
t = input()
cnt = 0

if s.replace("A", "") != t.replace("A", ""):
    print(-1)
else:
    s = deque(s)
    t = deque(t)
    while s or t:
        if s and t and s[0] == t[0]:
            s.popleft()
            t.popleft()
            #print("両方削除")
        elif s and s[0] == "A":
            s.popleft()
            cnt += 1
            #print("s削除")
        elif t and t[0] == "A":
            t.popleft()
            cnt += 1
            #print("t削除")
    print(cnt)

