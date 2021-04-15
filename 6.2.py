import random

n = int(input('Enter n: '))
m = int(input('Enter m: '))
k = int(input('Enter k: '))


M1 = [[random.randint(0, 100) for i in range(m)] for j in range(n)]
M2 = [[random.randint(0, 100) for i in range(k)] for j in range(m)]
M3=  [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(m):
        for p in range(k):
            M3[i][j] += M1[i][j] * M2[j][p]


print(M3)