#단순 배열 방문처리 문제
squares = []

max_x = 0
max_y = 0
for _ in range(4):
    a, b, c, d = map(int, input().split())
    max_x = max(max_x, c)
    max_y = max(max_y, d)
    squares.append([a, b, c, d])

visited = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

while squares:
    a, b, c, d = squares.pop()
    for i in range(b, d ):
        for j in range(a, c):
            visited[i][j] = 1

result = 0
for i in range(max_y + 1):
    for j in range(max_x + 1):
        result += visited[i][j]

print(result)