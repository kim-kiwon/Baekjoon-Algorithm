n, m, s = map(int, input().split())

sharks = [] #상어 저장
for _ in range(s):
    x, y, speed, direc, size = map(int, input().split())
    sharks.append((x-1, y-1, speed, direc, size))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

data = [[[] for _ in range(m)] for _ in range(n)] #각 칸에는 상어가 들어감.

for x, y, speed, direc, size in sharks:
    data[x][y].append((speed, direc, size))

result = 0
for j in range(m):
    #상어 잡기
    for i in range(n): #현재 낚시왕 위치에서 모든 행 확인하면서 상어 낚음
        if len(data[i][j]) != 0: #상어 존재시
            while data[i][j]: #상어 낚고
                speed, direc, size = data[i][j].pop()
                result += size
                sharks.remove((i, j, speed, direc, size)) #sharks에서 삭제
            break

    #상어 이동시키기
    temp_sharks = []
    while sharks:
        x, y, speed, direc, size = sharks.pop()
        data[x][y].remove((speed, direc, size)) # 원래 칸 삭제
        #이동후 좌표와 방향
        nx = x + speed * dx[direc]
        ny = y + speed * dy[direc]
        ndirec = direc
        #초과한 값에 따라 좌표 변경
        if direc == 1 and nx < 0:
            val = -nx #초과한값
            q, w = divmod(val, (n-1))
            if q % 2 == 0:
                ndirec = 2
                nx = w
            else:
                nx = n - 1 - w
        elif direc == 2 and nx >= n:
            val = nx - (n-1)
            q, w = divmod(val, (n - 1))
            if q % 2 == 0:
                ndirec = 1
                nx = n - 1 - w
            else:
                nx = w
        elif direc == 3 and ny >= m:
            val = ny - (m-1)
            q, w = divmod(val, (m - 1))
            if q % 2 == 0:
                ndirec = 4
                ny = m - 1 - w
            else:
                ny = w
        elif direc == 4 and ny < 0:
            val = -ny
            q, w = divmod(val, (m - 1))
            if q % 2 == 0:
                ndirec = 3
                ny = w
            else:
                ny = m - 1 - w
        #새로운 위치에 삽입
        data[nx][ny].append((speed, ndirec, size))
        #temp_shakrs에 삽입.
        temp_sharks.append((nx, ny, speed, ndirec, size))

    #상어 잡아먹기
    for i in range(n):
        for j in range(m):
            if len(data[i][j]) >= 2: #현재 칸에 상어가 여러마리면
                data[i][j].sort(key = lambda x : x[2], reverse = True) #사이즈 제일 큰 상어가 맨 앞에 오도록
            while len(data[i][j]) >= 2: #나머지 모두 삭제
                speed, direc, size = data[i][j].pop()
                temp_sharks.remove((i, j, speed, direc, size))
    sharks = []
    sharks.extend(temp_sharks)

print(result)