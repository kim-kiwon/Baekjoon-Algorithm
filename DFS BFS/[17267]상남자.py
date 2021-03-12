#BFS.
from collections import deque
n, m = map(int, input().split())
l, r = map(int, input().split())

q = deque()
visited = [[0] * m for _ in range(n)]

data =[]
for i in range(n):
    temp = list(map(int, list(input())))
    data.append(temp)
    for j in range(m):
        if data[i][j] == 2:
            q.append((i, j, l, r))
            visited[i][j] = 1
            data[i][j] = 0

while q:
    x, y, l_c, r_c = q.popleft()
    #위아래로 이동하면서 이동 가능 & 미방문시 방문 처리 후 큐 삽입
    #위로 이동
    nx = x
    while nx >= 0:
        if data[nx][y] == 1:
            break
        if visited[nx][y] == 0:
            visited[nx][y] = 1
            q.append((nx, y, l_c, r_c))
        nx -= 1
    #아래로이동
    nx = x
    while nx < n:
        if data[nx][y] == 1:
            break
        if visited[nx][y] == 0:
            visited[nx][y] = 1
            q.append((nx, y, l_c, r_c))
        nx += 1
    #l,r이 남아있을 경우 좌우로 이동. 미방문시 방문처리 후 큐 삽입
    if l_c >= 1:
        ny = y - 1
        if 0 <= ny < m:
            if visited[x][ny] == 0 and data[x][ny] == 0:
                visited[x][ny] = 1
                q.append((x, ny, l_c -1, r_c))
    if r_c >= 1:
        ny = y + 1
        if 0 <= ny < m:
            if visited[x][ny] == 0 and data[x][ny] == 0:
                visited[x][ny] = 1
                q.append((x, ny, l_c, r_c-1))

#방문한 칸 개수 출력
result = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            result += 1

print(result)