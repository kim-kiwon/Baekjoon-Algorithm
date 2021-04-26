'''
2의 n승 x 2의 n승 격자판.
data[r][c]는 r행 c열의 얼음 양.
1. 단계 L 결정.
2. 2의 L승 x 2의 L승 부분격자로 나눠서.
부분격자를 시계방향 90도 회전.
3. 얼음이있는칸 3개 이상 인접하지 않은 칸은 얼음양 1 줄어듦.
파이어스톰 총 q번시전.
'''

import sys

sys.setrecursionlimit(10**4)
n, q = map(int, input().split())
n = 2 ** n
data = [list(map(int, input().split())) for _ in range(n)]
levels = [int(input())] if q == 1 else list(map(int, input().split()))

def rotate_2d(data):
    d = len(data)
    temp = []
    zip_data = list(map(list, zip(*data)))
    for i in range(d):
        zip_data[i].reverse()
        temp.append(zip_data[i])
    return temp

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for level in levels:
    #2의 L승 x 2의 L승 만큼 rotate_2d 시키기.
    step = 2 ** level
    num = step / n
    for i in range(0, n, step):
        for j in range(0, n, step):
            temp = []
            for a in range(0, step):
                temp2 = []
                for b in range(0, step):
                    temp2.append(data[i+a][j+b])
                temp.append(temp2)
            temp = rotate_2d(temp)
            for a in range(0, step):
                for b in range(0, step):
                    data[i+a][j+b] = temp[a][b]
    #얼음 있는칸 녹이기
    melt = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            count = 0
            if data[i][j] == 0: continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if data[nx][ny] > 0:
                        count += 1
            if count < 3:
                melt[i][j] = 1

    for i in range(n):
        for j in range(n):
            data[i][j] -= melt[i][j]

visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    global count
    visited[x][y] = 1
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] > 0 and visited[nx][ny] == 0:
                dfs(nx, ny)
    return

sum_val = 0
max_count = 0
for i in range(n):
    sum_val += sum(data[i])
for i in range(n):
    for j in range(n):
        count = 0
        if data[i][j] == 1 and visited[i][j] == 0: dfs(i, j)
        max_count = max(max_count, count)

print(sum_val)
print(max_count)