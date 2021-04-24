'''
DFS + DP + 백트래킹 문제.
경로의 가지수를 세는게 아닌 경로의 깊이를 찾는것에 유의.
1. 모두 -1로 초기화. -1이 아닌 곳 -> dfs로 최대 동전 튕기기수 구한 곳.
2. 방문할 때마다 0으로 갱신. -1 아닌 칸 dfs로 방문 -> 해당칸에서 최대동전 튕기기값 이미 구해져있음 그대로 리턴.
3. 현재 칸은 max(현재 칸값, dfs로 구한 다음칸 튕긴수 + 1)
4. 동전을 한번도 못튕기는 곳에서는 한번 밖에 못튕김. dp 값 1로 갱신하고 그 값을 반환.
5. visited로 방문할때 마다 방문칸 저장. 다음 방문칸이 visited에 존재 -> 루프 생긴것. -1 출력 후 종료
'''
import sys

n, m = map(int, input().split())

dp = [[-1 for _ in range(m)] for _ in range(n)]

data = [list(input()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, visited):
    if dp[x][y] != -1: return dp[x][y]
    dp[x][y] = 0
    count = 0
    for i in range(4):
        nx = x + (int(data[x][y]) * dx[i])
        ny = y + (int(data[x][y]) * dy[i])
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 'H':
            if (nx, ny) in visited: print(-1); sys.exit()
            visited.append((nx, ny))
            dp[x][y] = max(dp[x][y], dfs(nx, ny, visited) + 1)
            visited.pop()
            count += 1
    if count == 0:
        dp[x][y] = 1
    if x == 0 and y ==0: return dp[x][y]
    return dp[x][y]

print(dfs(0, 0, [(0, 0)]))