n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

skill = []
for i in range(n):
    if A[i][0] == A[i][1] == 0:
        skill.append(i)

skillSet = set(skill)
for j in range(n//3):
    for i in range(n):
        if A[i][0]-1 in skillSet or A[i][1]-1 in skillSet:
            skillSet.add(i)
            
print(len(skillSet))