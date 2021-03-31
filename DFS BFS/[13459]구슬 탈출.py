#bfs방식 완전탐색.
#최단 회수
from collections import deque

n, m = map(int, input().split())

visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)] #rx, ry, bx ,by 4차원 방문배열

data = []
for i in range(n):
    data.append(list(input()))
    for j in range(m):
        if data[i][j] == 'R':
            rx, ry = i, j #빨간공 초기위치
        elif data[i][j] == 'B':
            bx, by = i, j #파란공 초기위치

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def move(x, y, dx, dy): #특정방향으로 벽 직전 or 구멍까지 이동
    count = 0 #이동 횟수. 두 공이 겹칠 시 활용하기 위해서
    while data[x+dx][y+dy] != '#' and data[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count

q = deque()
q.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = 1

def bfs():
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count > 10: #10번 넘게 이동시 종료.
            break
        for i in range(4):
            nrx, nry, rcount = move(rx, ry, dx[i], dy[i]) #빨간공의 다음위치.
            nbx, nby, bcount = move(bx, by, dx[i], dy[i]) #파란공의 다음위치.
            if data[nbx][nby] == 'O': #파란공 구멍에.
                continue #큐 삽입X
            if data[nrx][nry] == 'O': #빨간공 구멍에.
                print(1) #출력 후 종료.
                return
            if (nrx, nry) == (nbx, nby): #두 공이 같은 위치에.
                #이동 횟수 비교해서 더 많이 이동한 공을 한칸 뒤로
                if rcount > bcount:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if visited[nrx][nry][nbx][nby] == 0: #방문 아직 안했었으면
                visited[nrx][nry][nbx][nby] = 1 #방문처리하고
                q.append((nrx, nry, nbx, nby, count + 1)) #큐에 삽입.
    print(0)

bfs()