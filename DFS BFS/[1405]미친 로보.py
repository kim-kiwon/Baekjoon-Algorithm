#백트래킹 DFS

n, e_p, w_p, s_p, n_p = map(int, input().split()

visit = [[0] * 31 for _ in range(31)]
dan = 0 #단순할 확률.

#dx,dy 쌍과 val쌍 맞추기.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
val = ['e', 'w', 's', 'n']
arr = [] #이동경로 저장

def dfs(x, y, count, check):
    global dan, non_dan, n
    if count == n: #이동횟수 모두 사용. 확률 계산.
        percent = 1
        for i in arr:
            if i == 'n':
                percent *= n_p/100
            elif i == 'e':
                percent *= e_p/100
            elif i == 's':
                percent *= s_p/100
            elif i == 'w':
                percent *= w_p/100
        if check == 0:
            dan += percent
        return
    for i in range(4):
        visit[15][15] = 1
        nx = x + dx[i]
        ny = y + dy[i]
        if visit[nx][ny] == 1: #비단순. 제외
            continue
        else: #단순. DFS후 백트래킹
            arr.append(val[i])
            visit[nx][ny] = 1
            dfs(nx, ny, count + 1 ,0)
            visit[nx][ny] = 0
            arr.pop()

dfs(15, 15, 0, 0)
print(dan)