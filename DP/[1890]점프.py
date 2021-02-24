#DP문제

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1: #목적지 도착
            break
        ni = i + arr[i][j] #밑으로 점프
        nj = j + arr[i][j] #오른쪽으로 점프

        if ni < n:
            dp[ni][j] += dp[i][j]
        if nj < n:
            dp[i][nj] += dp[i][j]

print(dp[n-1][n-1])