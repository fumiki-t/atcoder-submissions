from itertools import permutations
import math

n = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(n)]

total_distance = 0
for perm in permutations(coordinates):
    for i in range(n-1):
        distance = ((perm[i][0] - perm[i+1][0]) ** 2 + (perm[i][1] - perm[i+1][1]) ** 2) ** 0.5
        total_distance += distance

print(total_distance / math.factorial(n))