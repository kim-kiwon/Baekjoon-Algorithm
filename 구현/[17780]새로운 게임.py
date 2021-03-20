import sys
n, k = map(int, input().split())

data = []
for _ in range(n):
    temp = []
    for _ in range(n):
        temp.append([0, []])
    data.append(temp)

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        data[i][j][0] = temp[j]
    #흰색 0. 빨강 1. 파랑 2.

pos = [] * k #말들의 현재 위치 저장
for i in range(k):
    r, c, direc = map(int, input().split())
    data[r-1][c-1][1].append(i)
    pos.append([r-1, c-1, direc-1])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

count = 0
while True:
    for i in range(k):
        x, y, d = pos[i]
        if i != data[x][y][1][0]:
            continue
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or data[nx][ny][0] == 2:
            if pos[i][2] == 0:
                pos[i][2] = 1
            elif pos[i][2] == 1:
                pos[i][2] = 0
            elif pos[i][2] == 2:
                pos[i][2] = 3
            else:
                pos[i][2] = 2
            d = pos[i][2]
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or data[nx][ny][0] == 2:
                continue
        for fv in data[x][y][1]:
            pos[fv][0] = nx
            pos[fv][1] = ny

        if data[nx][ny][0] == 1:
            data[x][y][1].reverse()
        data[nx][ny][1].extend(data[x][y][1])
        data[x][y][1] = []

        if len(data[nx][ny][1]) >= 4:
            count += 1
            print(count)
            sys.exit()
    count += 1
    if count > 1000:
        break
print(-1)