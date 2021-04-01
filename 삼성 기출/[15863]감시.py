#DFS 백트래킹
from copy import deepcopy
import sys

n, m = map(int, input().split())
data = []
cctvs = [] #CCTV 위치와 종류 저장.
for i in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    for j in range(m):
        if data[i][j] != 0 and data[i][j] != 6:
            cctvs.append((i, j, data[i][j]))

direcs = [[0], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
#각 CCTV 유형별 감시 가능한 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def see(x, y, data, d): #CCTV 종류에 따라 d 안의 모든 방향을 감시
    for i in d:
        nx = x
        ny = y
        while 1:
            nx += dx[i]
            ny += dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m: break
            if data[nx][ny] == 6 : break
            if data[nx][ny] == 0 : data[nx][ny] = '#'

result = sys.maxsize
def dfs(data, count):
    global result
    temp = deepcopy(data) #백트래킹 하기위해 백업
    if count == len(cctvs): #끝까지 도달
        score = 0
        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    score += 1
        result = min(result, score)
        return
    x, y, num = cctvs[count] #count번째 cctv 가져옴
    for i in direcs[num]: #해당 cctv의 방향을 바꿔나감
        see(x, y, data, i) #감시
        dfs(data, count + 1) #DFS시키고
        data = deepcopy(temp) #복구

dfs(data, 0)
print(result)