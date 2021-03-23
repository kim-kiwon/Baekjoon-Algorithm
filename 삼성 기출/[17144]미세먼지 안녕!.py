n, m, t = map(int, input().split())

mx1 = [0, 0]
mx2 = [0, 0]

data = [[[0, 0] for _ in range(m)] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        data[i][j][0] = temp[j]
        if data[i][j][0] == -1:
            if mx1[0] == 0:
                mx1 = [i, j]
            else:
                mx2 = [i, j]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


while t > 0:
    for i in range(n):
        for j in range(m):
            if data[i][j][0] >= 5:
                cd = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and data[nx][ny][0] != -1:
                        data[nx][ny][1] += (data[i][j][0] // 5)
                        cd += 1
                data[i][j][1] -= ((data[i][j][0]//5) * cd)

    for i in range(n):
        for j in range(m):
            data[i][j][0] += data[i][j][1]
            data[i][j][1] = 0

    temp1, temp2, temp3 = data[mx1[0]][m - 1][0], data[0][m - 1][0], data[0][0][0]

    for j in range(m-1, 0, -1):
        if j == 1:
            data[mx1[0]][j][0] = 0
        else:
            data[mx1[0]][j][0] = data[mx1[0]][j-1][0]

    for i in range(0, mx1[0]):
        data[i][m-1][0] = data[i+1][m-1][0]

    for j in range(m - 1):
        data[0][j][0] = data[0][j + 1][0]

    for i in range(mx1[0] - 1, 0, -1):
        data[i][0][0] = data[i-1][0][0]

    data[mx1[0] - 1][m - 1][0] = temp1
    data[0][m-2][0] = temp2
    data[1][0][0] = temp3

    temp1, temp2, temp3 = data[mx2[0]][m-1][0], data[n-1][m-1][0], data[n-1][0][0]
    for j in range(m-1, 0, -1):
        if j == 1:
            data[mx2[0]][j][0] = 0
        else:
            data[mx2[0]][j][0] = data[mx2[0]][j-1][0]
    for i in range(n-1, mx2[0], -1):
        data[i][m-1][0] = data[i-1][m-1][0]
    for j in range(m-1):
        data[n-1][j][0] = data[n-1][j+1][0]
    for i in range(mx2[0] + 1, n-1):
        data[i][0][0] = data[i+1][0][0]

    data[mx2[0] + 1][m-1][0] = temp1
    data[n-1][m-2][0] = temp2
    data[n-2][0][0] = temp3

    t -= 1

result = 0
for i in range(n):
    for j in range(m):
        result += data[i][j][0]

print(result + 2)