#1600번과 유사. 3차원 방문배열.
from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    temp = list(map(int, list(input())))
    arr.append(temp)

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] #3차원 방문배열.
                                                #[x][y][0] : 벽부수기 아직 안쓰고 도달한 최소거리. [x][y][1] : 벽부수기 쓰고 도달한 최소거리.
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0)) #벽부수기 안쓰고 시작점 삽입.
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1: #목적지 도착.
            return visited[x][y][z] #해당 방문배열 값 return. (시작점 포함이므로 -1 생략)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
                if z == 0: #벽부수기 아직 안썼으면. 벽부수기 사용 후 벽 위치로 이동가능.
                    if arr[nx][ny] == 1 and visited[nx][ny][1] == 0:
                        q.append((nx, ny, 1))
                        visited[nx][ny][1] = visited[x][y][0] + 1
    return(-1) 
print(bfs())