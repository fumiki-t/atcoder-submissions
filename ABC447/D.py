s = input()
cnt = 0

a_idx = s.find("A")
b_idx = s.find("B", a_idx+1)
c_idx = s.find("C", b_idx+1)

while a_idx != -1 and b_idx != -1 and c_idx != -1:
    cnt += 1
    a_idx = s.find("A", a_idx+1)
    if a_idx <= b_idx:
        b_idx = s.find("B", b_idx+1)
    else:
        b_idx = s.find("B", a_idx+1)
    if b_idx <= c_idx:
        c_idx = s.find("C", c_idx+1)
    else:
        c_idx = s.find("C", b_idx+1)

print(cnt)
