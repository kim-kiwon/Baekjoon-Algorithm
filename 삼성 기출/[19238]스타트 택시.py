'''
아이디어
1. 승객 고르기
현재 택시 위치에서 BFS. 여러명이면 ?
queue 를 정렬해나가자. 거리값 -> x 값 -> y 값순서로.
승객 위치 만나면 연료값 뺴고 나르기 시작.

2. 승객 나르기
목적지 까지 BFS.
시작 택시 연료보다 중간에 바닥나면 종료.

벽에 막혀서 승객 못태우고 못도착할 경우 대비 flag 만들기.
'''
from collections import deque
import sys
n, p, f = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

sx, sy = map(int, input().split())
sx -= 1; sy -= 1

person = dict()
for _ in range(p):
    a, b, c, d = map(int, input().split())
    person[(a-1, b-1)] = [c-1, d-1]
    data[a-1][b-1] = 2

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for _ in range(p):
    found, take = 0, 0
    q = []
    q.append((sx, sy, 0))
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    destx, desty = 0, 0

    while q:
        q = list(q)
        q.sort(key = lambda x : (x[2], x[0], x[1]))
        q = deque(q)
        x, y, c = q.popleft()
        if data[x][y] == 2:
            sx = x; sy = y;
            f -= c
            data[x][y] = 0
            destx, desty = person[(x, y)]
            found = 1
            break
            if f <= 0:
                print(-1)
                sys.exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and data[nx][ny] != 1:
                    q.append((nx, ny, c+1))
                    visited[nx][ny] = 1
    if found == 0: print(-1); sys.exit();

    q = deque()
    q.append((sx, sy, 0))
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    while q:
        x, y, c = q.popleft()
        if x == destx and y == desty:
            if f < c:
                print(-1)
                sys.exit()
            f += c
            sx, sy = destx, desty
            take = 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and data[nx][ny] != 1:
                    q.append((nx, ny, c+1))
                    visited[nx][ny] = 1
    if take == 0: print(-1); sys.exit();
print(f)