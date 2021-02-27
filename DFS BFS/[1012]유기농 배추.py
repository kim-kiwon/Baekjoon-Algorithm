#DFS. 재귀에러. setrecursionlimit 함수로 재귀호출수 증가필요.
import sys

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if arr[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True

sys.setrecursionlimit(2000) #디폴트 = 1000

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1
    print(count)