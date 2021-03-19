#요구조건에 따라 구현

n, m, x, y, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

orders = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for o in orders:
    #가능하다면 현재 좌표 변화
    nx = x + dx[o]
    ny = y + dy[o]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x = nx
    y = ny

    #주사위 굴림에 따라 각 면의 위치 변화
    if o == 1:
        temp = dice[5]
        dice[5] = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1]
        dice[1] = temp
    elif o == 2:
        temp = dice[5]
        dice[5] = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[3]
        dice[3] = temp
    elif o == 3:
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[4]
        dice[4] = dice[5]
        dice[5] = temp
    elif o == 4:
        temp = dice[0]
        dice[0] = dice[5]
        dice[5] = dice[4]
        dice[4] = dice[2]
        dice[2] = temp

    #지도값에 따라 바닥값 & 지도값 변화
    if data[x][y] == 0:
        data[x][y] = dice[5]
    else:
        dice[5] = data[x][y]
        data[x][y] = 0
    print(dice[2])