#DFS로 할경우 시간초과 or 메모리초과.
#이럴땐 BFS로 구현해보자.
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
arr = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        arr[i][j][0] = temp[j]


def melt(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny][0] == 0:
                count += 1
    arr[x][y][1] = count

def check(x, y): #BFS로 구현
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny][0] != 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

year = 0
while True:
    year += 1
    visited = [[0] * m for _ in range(n)]
    count = 0
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j][0] != 0:
                melt(i, j)
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j][0] != 0:
                arr[i][j][0] -= arr[i][j][1]
                if arr[i][j][0] < 0 : arr[i][j][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j][0] != 0 and visited[i][j] == 0:
                check(i, j)
                count += 1
    if count >= 2:
        print(year)
        break
    elif count == 0:
        print(0)
        break