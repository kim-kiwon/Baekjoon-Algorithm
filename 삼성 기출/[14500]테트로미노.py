#DFS 백트래킹 + 십자가형 탐지
n, m = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

answer = 0

visited = [[0] * m for _ in range(n)]

def dfs(x, y, temp, count, sum_val):
    global answer
    if count == 4:
        answer = max(answer, sum_val)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] == 1:
            continue
        visited[nx][ny] = 1
        temp.append((nx, ny))
        dfs(nx, ny, temp, count + 1, sum_val + data[nx][ny])
        visited[nx][ny] = 0
        temp.pop()

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, [], 1, data[i][j])
        visited[i][j] = 0
        #ㅗ 모양은 DFS로 불가능. 중간에서 올라가는 모양이므로
        if j + 2 < m:
            val = data[i][j] + data[i][j+1] + data[i][j+2]
            if i + 1 < n:
                val1 = val + data[i+1][j+1]
                answer = max(val1,answer)
            if i - 1 >= 0:
                val2 = val + data[i-1][j+1]
                answer = max(val2, answer)
        if i + 2 < n:
            val = data[i][j] + data[i+1][j] + data[i+2][j]
            if j + 1 < m:
                val1 = val + data[i+1][j+1]
                answer = max(val1, answer)
            if j - 1 >= 0:
                val2 = val + data[i+1][j-1]
                answer = max(val2, answer)
print(answer)