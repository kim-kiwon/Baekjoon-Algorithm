#백트래킹

import copy
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def virus(x, y, temp):
    if x < 0 or x >= n or y < 0 or y >= m or temp[x][y] == 1:
        return
    if temp[x][y] == 0 or temp[x][y] == 2:
        temp[x][y] = 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            virus(nx, ny, temp)

answer = 0
def solve(r, count):
    global answer
    if count == 3:
        temp = copy.deepcopy(arr)
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j, temp)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        answer = max(answer, score)
        return
    for i in range(r, n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                solve(i, count + 1)
                arr[i][j] = 0

solve(0, 0)
print(answer)