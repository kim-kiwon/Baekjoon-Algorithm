N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
ans = 10000
dir = [0, 0, 0, 1, -1]
dic = [0, 1, -1, 0, 0]
def check(r, c):
    for i in range(5):
        if visit[r+dir[i]][c+dic[i]] == 1:
            return False
    return True

def dfs(count, r):
    global ans
    if count == 3:
        summ = 0
        for i in range(N):
            for j in range(N):
                if visit[i][j] == 1:
                    summ += arr[i][j]
        if summ < ans:
            ans = summ
        return
    for i in range(r,N-1):
        for j in range(1,N-1):
            if check(i, j):
                for k in range(5):
                    visit[i+dir[k]][j+dic[k]] = 1
                dfs(count+1, i)
                for k in range(5):
                    visit[i + dir[k]][j + dic[k]] = 0

dfs(0, 1)
print(ans)