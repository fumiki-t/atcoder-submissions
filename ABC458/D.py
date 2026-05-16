from sortedcontainers import SortedList
x = int(input())
q = int(input())
data = SortedList([x])

for _ in range(q):
    a, b = map(int, input().split())
    data.add(a) 
    data.add(b)

    print(data[len(data) // 2])
