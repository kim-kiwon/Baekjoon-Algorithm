N = int(input())

visit = [0 for _ in range(N)]

def check(c):
    for i in range(c):
        if visit[i] == visit[c] or abs(visit[i]-visit[c]) == abs(i - c):
            return False
    return True

ans = 0
def dfs(row):
    global ans
    if row == N:
        ans += 1
        return
    for i in range(N):
        visit[row] = i
        if check(row):
            dfs(row+1)
            visit[row] = 0

dfs(0)
print(ans)