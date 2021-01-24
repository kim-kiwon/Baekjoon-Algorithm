#DP 편집거리 알고리즘.

n, m = map(int, input().split())
data = input()
answer = input()

dp = [[0] * (len(data)+1) for _ in range(len(answer) + 1)]

for i in range(len(data) + 1):
    dp[0][i] = i

for i in range(len(answer) + 1):
    dp[i][0] = i

def exception(ans, data):
    if data == 'i':
        if ans == 'j' or ans == 'l':
            return True
    if data == 'v':
        if ans == 'w':
            return True
    return False

for i in range(1, len(answer) + 1):
    for j in range(1, len(data) + 1):
        if (answer[i-1] == data[j-1]) or exception(answer[i-1], data[j-1]):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(dp[m][n])