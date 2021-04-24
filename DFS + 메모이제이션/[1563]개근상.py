'''
풀이
그냥 DFS로 풀면 3의 N승가지 경우의수 -> 시간초과
메모이제이션 써야함.
'''
import sys
sys.setrecursionlimit(10**6)
n = int(input())

dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
# dp[d][l][a]
# 현 날짜에서 지각수와 연속결석수. 이상태로 n일까지 개근상 받을 수 있는 경우의 수를 저장해놓자.

def dfs(d, l, a):
    if l == 2 or a == 3:
        return 0
    if d == n:
        return 1
    if dp[d][l][a] == -1:
        dp[d][l][a] = dfs(d + 1, l, 0) + dfs(d + 1, l + 1, 0) + dfs(d + 1, l, a + 1)
    return dp[d][l][a]

print((dfs(0 ,0 ,0))% 1000000)
print(dp)