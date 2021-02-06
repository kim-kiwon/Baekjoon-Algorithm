#bfs 이용.
from collections import deque

m, n = map(int, input().split())
weldone = [] #다 익은 토마토 위치 저장.
arr = [] #전체 배열
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 1:
            weldone.append((i, j))
    arr.append(temp)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def allripen(): #안익은 토마토 존재하는지 확인 함수
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                return False
    return True

flag = True
if allripen() == True: #시작부터 안익은 토마토 없으면
    print(0)
    flag = False #결과 출력 후 flag 변경.

q = deque(weldone)
while q and flag:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1 #bfs로 탐색 위치 = 전 위치 +1
                q.append((nx, ny)) #deque에 추가
max_val = -1e9
if flag: #시작할때 안익은 토마토 존재
    if allripen() == True: #bfs종료후 안익은 토마토 없음.
        for i in range(n):
            for j in range(m):
                max_val = max(max_val, arr[i][j])
        print(max_val - 1) #최대값 - 1 출력 (익은 토마토 초기값 1이므로 -1 해줌)
    else: #bfs종료후 안익은 토마토 존재
        print(-1)