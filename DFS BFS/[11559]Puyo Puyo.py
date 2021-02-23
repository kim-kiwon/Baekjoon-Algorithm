#bfs + 이동
from collections import deque

arr = []
for i in range(12):
    arr.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

turn_flag = False #이번 턴에 뿌요제거가 한번이라도 있었는가.
flag = False #뿌요제거가 발생하였는가.

def bfs(x, y):
    global flag
    flag = False
    temp = [] #4개 이상 모였을때 삭제할 뿌요들
    count = 1 #bfs 개수
    q = deque()
    q.append((x, y, arr[x][y]))
    temp.append((x, y))
    while q:
        x, y, val = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if (nx, ny) not in temp  and arr[nx][ny] == val:
                    count += 1
                    temp.append((nx, ny)) #bfs로 탐색하면서 모인 뿌요에 삽입.
                    q.append((nx, ny, arr[nx][ny]))
    if count >= 4: #카운트가 4개되면
        for x, y in temp: #모인 뿌요 모두 삭제.
            arr[x][y] = '.'
            flag = True #삭제 발생 True로

def movepuyo(): #아래 빈 뿌요들 바닥으로 내리는 함수.
    temp = [[] for _ in range(6)] #각 열별로 빈칸이 아닌 뿌요들 저장.
    for j in range(6):
        for i in range(12):
            if arr[i][j] != '.':
                temp[j].append(arr[i][j])
                arr[i][j] = '.'
    for j in range(6): #저장한 뿌요들 끝부터 삽입.
        for i in range(11, -1, -1):
            if len(temp[j]) == 0: break
            arr[i][j] = temp[j].pop()

result = 0
while True:
    turn_flag = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                bfs(i, j)
                if flag == True: #한번이라도 제거 발생시
                    turn_flag = True #이번턴 플래그 True
    movepuyo()
    if turn_flag == False: #한번도 제거 없었으면 종료.
        break
    result += 1

print(result)