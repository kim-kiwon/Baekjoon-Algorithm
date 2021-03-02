#DFS+BFS.
#DFS:섬별로 번호 부여하기 위해.
#BFS:다른섬으로의 최단거리 구하기 위해.

from collections import deque
import sys

sys.setrecursionlimit(50000)

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 1 #섬에 부여할 번호
visited = [[0] * n for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if arr[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        arr[x][y] = count #각 섬에 번호 부여
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            count += 1

min_val = int(1e9)
for i in range(1, count+1): #모든 섬에 대하여 수행
    visited = [[0] * n for _ in range(n)]
    q = deque() #bfs 활용
    for i in range(n): #자신 섬 모든 좌표 우선 큐에 삽입 및 방문처리.
        for j in range(n):
            if arr[i][j] == count:
                q.append((i, j))
                visited[i][j] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if arr[nx][ny] == 0: #바다면.
                    visited[nx][ny] = visited[x][y] + 1 #visited 값을 + 1
                    q.append((nx, ny))
                else: #다른섬 도착했으면
                    min_val = min(visited[x][y] - 1, min_val) #전 visited 값 -1. 즉 현재칸 BFS값 -2. (도착점 제외, 1부터시작해서)
                    break
print(min_val)