'''
주의할 점
1. 현재 말의 위의 말들만 함께 이동. 아래 말들은 그대로.
2. 다음 칸의 빨간칸이라면 뒤집고나서 이동.
3. 한번 파란칸 후에 반대로 이동한다면. 반대로 이동 후 빨간칸일 경우도 고려해주어야함.
'''
import sys
n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    # 0 : 흰. 1: 빨. 2: 파

h_data = [[[] for _ in range(n)] for _ in range(n)]

horses = []
for i in range(k):
    r, c, d = map(int, input().split())
    horses.append([r - 1, c - 1, d - 1])
    h_data[r-1][c-1].append(i)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

count = 0
while True:
    count += 1
    for i in range(k):
        x, y, d = horses[i]

        #다음칸으로
        nx = x + dx[d]
        ny = y + dy[d]

        #이동할 칸 확인하기.
        if (nx < 0 or nx >= n or ny < 0 or ny >= n) or data[nx][ny] == 2:
            if horses[i][2] == 0:
                horses[i][2] = 1
            elif horses[i][2] == 1:
                horses[i][2] = 0
            elif horses[i][2] == 2:
                horses[i][2] = 3
            elif horses[i][2] == 3:
                horses[i][2] = 2
            d = horses[i][2]
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx < 0 or nx >= n or ny < 0 or ny >= n) or data[nx][ny] == 2:
                continue

        for a in range(len(h_data[x][y])):
            if h_data[x][y][a] == i:
                break
        move_val = h_data[x][y][a:] #i의 위에있는 놈들
        h_data[x][y] = h_data[x][y][:a] #i의 아래놈들
        
        #빨간땅이면 뒤집어주기
        if data[nx][ny] == 1:
            move_val.reverse()

        #전칸 놈들 다 이동
        #horses 바꿔주기. h_data 바꿔주기.
        for f in move_val:
            horses[f][0] = nx
            horses[f][1] = ny
        h_data[nx][ny].extend(move_val)

        if len(h_data[nx][ny]) >= 4:
            print(count)
            sys.exit()
    if count == 1000:
        print(-1)
        sys.exit()

