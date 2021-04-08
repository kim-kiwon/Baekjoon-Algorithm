n, t, k = map(int, input().split())

plus = []
for i in range(n):
    plus.append(list(map(int, input().split())))

data = [[[[] for _ in range(2)]for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        data[i][j][0] = 5

for _ in range(t):
    x, y, z = map(int, input().split())
    data[x-1][y-1][1].append(z)
#data[x][y][0] : x, y 의 영양분
#data[x][y][1] : [x, y에 존재하는 나무들의 나이]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


for z in range(k):
    for i in range(n):
        for j in range(n):
            if data[i][j][1]:
                data[i][j][1].sort()
                temp_tree, dead_tree = [], 0
                for age in data[i][j][1]:
                    if age <= data[i][j][0]:
                        data[i][j][0] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += age // 2
                data[i][j][0] += dead_tree
                data[i][j][1] = temp_tree

    for i in range(n):
        for j in range(n):
            if data[i][j][1]:
                for age in data[i][j][1]:
                    if age % 5 == 0:
                        for k in range(8):
                            nx = i + dx[k]
                            ny = j + dy[k]
                            if 0 <= nx < n and 0 <= ny < n:
                                data[nx][ny][1].append(1)
    for i in range(n):
        for j in range(n):
            data[i][j][0] += plus[i][j]

result = 0
for i in range(n):
    for j in range(n):
        result += len(data[i][j][1])

print(result)