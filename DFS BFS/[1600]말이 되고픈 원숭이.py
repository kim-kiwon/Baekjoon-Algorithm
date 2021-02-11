from collections import deque

k = int(input()) #말처럼 움직일 수 있는 횟수
w, h = map(int, input().split()) #보드판 크기
board = [] #보드판
for i in range(h):
    temp = list(map(int, input().split()))
    board.append(temp)
visited = [[[0 for _ in range(k+1)] for _ in range(w)] for _ in range(h)] #방문 배열을 3차원으로 생성.
                                                                          #말처럼 이동한 횟수를 저장하기 위해.

#원숭이 처럼 이동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

#말처럼 이동
dx2 = [-2, -1, 1, 2, 2, 1, -1, -2]
dy2 = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
    q = deque()
    visited[x][y][0] = 1
    q.append((x, y, 0))
    while q:
        x, y, z = q.popleft() #x,y : 좌표. z:말처럼 이동한 횟수

        #오른쪽 최하단 도달시 해당 방문배열값 -1 출력. (처음 값이 1이므로 -1 해줌.)
        #bfs에 따라 원숭이,말 포함 최단경로가 출력되게 된다.
        if x == h-1 and y == w-1:
            return visited[x][y][z] -1

        #원숭이처럼 이동 bfs
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][z] == 0 and board[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

        #말처럼 이동 bfs
        if z < k:
            for i in range(8):
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if visited[nx][ny][z+1] == 0 and board[nx][ny] == 0:
                        visited[nx][ny][z+1] = visited[x][y][z] + 1
                        q.append((nx, ny, z + 1))

    #큐가 빌 때까지 도달 못할시 -1 리턴
    return -1

print(bfs(0, 0))