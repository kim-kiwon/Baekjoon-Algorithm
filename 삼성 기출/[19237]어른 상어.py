#구현
n, m, k = map(int, input().split())

prefer = [[[0] for _ in range(5)] for _ in range(m + 1)]
# prefer[a][b] : a번째 상어가 b방향 보고있을때 우선순위. 4개 들어잇음.
data = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

sharks = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        data[i][j][0] = temp[j]

# data[i][j][0] = 존재하는 상어들
# data[i][j][1] = 냄새 주인
# data[i][j][2] = 냄새시간

direc = [0] + list(map(int, input().split()))

for i in range(m):
    for j in range(4):
        prefer[i + 1][j + 1] = list(map(int, input().split()))

# 초창기 냄새뿌리기
for i in range(n):
    for j in range(n):
        val = data[i][j]
        if val[0] != 0:
            val[1] = val[0]
            val[2] = k


def check():
    count = 0
    for i in range(n):
        for j in range(n):
            if data[i][j][0] != 0:
                count += 1
    if count == 1:
        return True
    else:
        return False


dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def find_direc(sn, x, y, d):
    can_go = []
    can_go2 = []
    for i in range(1, 5):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny][1] == 0:
                can_go.append(i)
            if data[nx][ny][1] == sn:
                can_go2.append(i)
    if can_go:
        for val in prefer[sn][d]:
            if val in can_go:
                return (x + dx[val], y + dy[val], val)
    if can_go2:
        for val in prefer[sn][d]:
            if val in can_go2:
                return (x + dx[val], y + dy[val], val)
    else:
        return (x, y, d)

time = 0
while True:
    if time >= 1000: time = -1; break;
    time += 1

    # 냄새뿌림
    for i in range(n):
        for j in range(n):
            val = data[i][j]
            if val[0] != 0:
                val[1] = val[0]
                val[2] = k

    # 상어들 찾아서 sharks에 넣음.
    for i in range(n):
        for j in range(n):
            if data[i][j][0] != 0:
                sharks.append((data[i][j][0], i, j, direc[data[i][j][0]]))

    # 모든 sharks에 대해 pop하면서 이동시킴.
    while sharks:
        sn, x, y, d = sharks.pop()
        nx, ny, nd = find_direc(sn, x, y, d)
        data[x][y][0] = 0
        if data[nx][ny][0] == 0:
            data[nx][ny][0] = sn
            direc[sn] = nd
        else:
            data[nx][ny][0] = min(data[nx][ny][0], sn)
            direc[sn] = nd
    # 냄새 줄어듦
    for i in range(n):
        for j in range(n):
            if data[i][j][1] != 0:
                data[i][j][2] -= 1
                if data[i][j][2] == 0:
                    data[i][j][1] = 0

    if check(): break

print(time)