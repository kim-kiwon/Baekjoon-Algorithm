#DFS + 메모이제이션
import sys
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]
#방문 확인 위해 -1로 설정.

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    elif dp[x][y] != -1: #여기 방문했었으면. 여기서부터 종점까지 갈수 있는 경로 수 위로 반환.
        return dp[x][y]
    dp[x][y] = 0 #방문완료. 여기서 종점까지 갈 수있는 수 0으로 초기화
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] < data[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]
print(dfs(0, 0))