#삼차원 배열 BFS
from collections import deque

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

while True:
    l, r, c = map(int, input().split())
    if (l, r, c) == (0, 0, 0):
        break
    arr = []
    visited = []
    for f in range(l): #삼차원 배열 입력 및 시작, 끝 저장
        temp = []
        for i in range(r+1):
            temp2 = list(input())
            if i == r:
                arr.append(temp)
                break
            for j in range(c):
                if temp2[j] == 'S':
                    sval = (f, i, j)
                elif temp2[j] == 'E':
                    dval = (f, i, j)
            temp.append(temp2)

    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    escape = 0 #큐 빌때까지 탈출 하였는지 여부
    q = deque()
    q.append(sval)
    visited[sval[0]][sval[1]][sval[2]] = 1
    while q:
        z, x, y = q.popleft()
        if (z, x, y) == dval:
            print("Escaped in %d minute(s)." % (visited[z][x][y] - 1))
            escape = 1
            break
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz <l and 0 <= nx < r and 0 <= ny < c:
                if visited[nz][nx][ny] == 0 and arr[nz][nx][ny] != '#':
                    q.append((nz, nx, ny))
                    visited[nz][nx][ny] = visited[z][x][y] + 1
    if escape == 0:
        print("Trapped!")