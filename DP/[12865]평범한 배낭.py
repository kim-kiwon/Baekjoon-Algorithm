#DP. 냅색 알고리즘
n, k = map(int, input().split())

data = []
for _ in range(n):
    w, v = map(int, input().split())
    data.append([w, v])

data = [[0]] + data

dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1, n+1): #모든 물건에 대해
    now_w = data[i][0] #i번째 물건 무게
    now_h = data[i][1] #i번째 물건 가치
    for j in range(k + 1): #모든 무게에 대해
        if now_w <= j: #i번째 물건을 넣을 수 있다면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-now_w] + now_h) #i번째 물건 안넣은거 vs i번째 물건 넣은거 중 가치 더 큰것.
        else:
            dp[i][j] = dp[i-1][j] #못넣으면 i번째 물건 안넣은거 그대로

print(dp[n+1][k+1])
