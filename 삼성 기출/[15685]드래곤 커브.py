#구현
data = [[0] * (101) for _ in range(101)]
n = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


for _ in range(n):
    y, x, d, g = map(int, input().split()) #x,y 가 바뀐것에 유의
    data[x][y] = 1 #시작점 1로
    moves = [d] #이동 좌표들 삽입.
    for _ in range(g):
        lm = len(moves)
        for i in range(lm - 1, -1, -1): #뒤에서부터 +1 한뒤 %4 삽입.
            moves.append((moves[i] + 1) % 4)
    for i in moves: #moves 좌표에 따라 이동해나감.
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            data[nx][ny] = 1
            x, y = nx, ny
        else:
            break

result = 0
for i in range(0, 100): #둘러싸인 개수 체크
    for j in range(0, 100):
        if data[i][j] and data[i+1][j] and data[i][j+1] and data[i+1][j+1]:
            result += 1

print(result)