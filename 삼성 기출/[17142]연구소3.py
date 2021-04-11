'''
주의할것
1. 비활성 바이러스가 마지막 칸이면 그게 max값이 되지 않도록.
2. 비활성 바이러스가 중간에 있다면 빈칸처럼 쓸 수 있도록
'''
from collections import deque
from itertools import combinations
from copy import deepcopy
n, v = map(int, input().split())

virus_og = []
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        if data[i][j] == 2:
            virus_og.append((i, j))
            data[i][j] = 0
        elif data[i][j] == 1:
            data[i][j] = -1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

virus_choose = list(combinations(virus_og, v))

result = int(1e9)
for v_list in virus_choose:
    q = deque()
    visited = deepcopy(data)
    #활성 바이러스 방문처리 및 큐 삽입
    for v_val in v_list:
        x, y = v_val
        visited[x][y] = 1
        q.append((x, y))
    #활성 바이러스 전파
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    continue
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
        if (x, y) in virus_og: #비활성화 바이러스면 방문값 초기화. 이게 마지막이면 최대값으로 안걸리게 하기위함
            visited[x][y] = 1
    max_val = max(map(max, visited))
    max_val -= 1 #모두 퍼지는 시간.

    #while 문 끝나고도 0 존재하면 -1 출력.
    cant = 0
    for i in range(n):
        if visited[i].count(0) != 0: cant = 1; break;
    if cant == 1: continue

    result = min(result, max_val)

if result == 1e9:
    print(-1)
else:
    print(result)