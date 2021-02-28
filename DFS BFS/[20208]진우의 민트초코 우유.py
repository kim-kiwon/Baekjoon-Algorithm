#dfs + 백트래킹
n, m, h = map(int, input().split())

milks = [] #우유 위치
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            hx, hy = i, j #시작지점
        elif temp[j] == 2:
            milks.append((i, j))
    arr.append(temp)
ans = 0

def dfs(sx, sy, hp, count):
    global ans, hx, hy
    for x, y in milks: #우유들에 대해
        if arr[x][y] == 2: #해당 우유 마셨으면
            go = abs(sx - x) + abs(sy - y) #가는 거리 계산
            if go <= hp: #먹을 수 있으면 섭취 후 백트래킹
                arr[x][y] = 0
                dfs(x, y, hp + h - go, count + 1)
                arr[x][y] = 2
    if abs(sx - hx) + abs(sy - hy) <= hp: #해당 번째에 돌아갈 수 있다면 ans갱신
        ans = max(ans, count)
        return
dfs(hx, hy, m, 0)
print(ans)