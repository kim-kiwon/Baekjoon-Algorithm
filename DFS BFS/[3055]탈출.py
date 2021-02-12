#bfs 이용
from collections import deque

r, c = map(int, input().split())

visited = [[0] * c for _ in range(r)] #방문 배열. 고슴도치 이동에 사용

arr = [] #지도 배열
q = deque() #bfs에 사용할 queue
dochix, dochiy = 0, 0 #고슴도치 좌표(S)
destx, desty = 0, 0 #비버굴 좌표(D)

for i in range(r):
    temp = list(input())
    for j in range(c):
        if temp[j] == '*': #물 좌표 큐에 먼저 삽입.
            q.append((i, j, 1))
        elif temp[j] == 'S': #고슴도치 좌표. 큐에 삽입 할 것이지만. 물 좌표들보다 늦게 삽입해야되므로 우선 저장.
            dochix = i
            dochiy = j
            visited[i][j] = 1
        elif temp[j] == 'D': #목적지 좌표. bfs 탈출 조건에 활용.
            destx = i
            desty = j
    arr.append(temp)

q.append((dochix, dochiy, 2)) #고슴도치 좌표 삽입. 물보다 늦게 삽입해야 물이 퍼질 위치에 고슴도치가 못 가도록 할 수 있다.

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while q:
        x, y, t = q.popleft() #t = 물인지. 고슴도치인지.
        if x == destx and y == desty: #목적지 도착시 이동 수 반환.
            return visited[x][y] - 1
        if t == 1: #큐에서 꺼낸게 물좌표면.
            for i in range(4): #물 전파.
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if arr[nx][ny] == '.' or arr[nx][ny] == 'S':
                        arr[nx][ny] = '*'
                        q.append((nx, ny, 1))
        elif t == 2: #큐에서 꺼낸게 고슴도치이면.
            for i in range(4): #이동 가능한 곳으로 고슴도치 bfs.
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny, 2))
    return "KAKTUS" #큐 빌때까지 목적지 못가면 KAKTUS 반환.

print(bfs())

