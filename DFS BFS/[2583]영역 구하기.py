#dfs. 재귀 깊이 제한 조절에 유의하자
import sys
sys.setrecursionlimit(50000)

count = 0
val = [0]
def dfs(x, y):
    global count
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if visited[x][y] == 0 and arr[x][y] == 0:
        val[count] += 1
        visited[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

m, n, k = map(int, input().split())

arr = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    for i in range(y0, y1):
        for j in range(x0, x1):
            arr[i][j] = 1

for i in range(m):
    for j in range(n):
        if dfs(i, j) == True:
            count += 1
            val.append(0)

val.pop()
val.sort()

print(count)
for i in val:
    print(i, end = ' ')
print()