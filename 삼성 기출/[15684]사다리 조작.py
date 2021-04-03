#dfs 완전탐색
import sys
n, m, h = map(int, input().split())

link = [[0] * h for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    link[b-1][a-1] = 1 #i행 j열. i와 i+1 선이 j번째 가로선에서 연결.


def check(): #모든 선이 자기 위치로 가나 체크
    for i in range(n):
        now = i
        for j in range(h):
            if link[now][j] == 1:
                now += 1
            elif now - 1 >= 0 and link[now-1][j] == 1:
                now -= 1
        if now != i:
            return False
    return True

result = sys.maxsize
def dfs(r, count, max_count):
    global result
    if count == max_count: #max_count만큼 가로선 추가.
        if check(): #조건 만족하면 갱신
            result = min(result, count)
        return
    for i in range(r, n-1):
        for j in range(h):
            if i - 1 >= 0 and link[i - 1][j] == 1: continue #왼쪽에 가로선 이미 존재
            if i + 1 < n and link[i + 1][j] == 1: continue #오른쪽에 가로선 이미 존재
            if link[i][j] == 1: continue #현재 위치에 가로선 이미 존재
            link[i][j] = 1
            dfs(i, count + 1, max_count) #DFS 시간단축용. 현재 행부터 시작하게
            link[i][j] = 0

for i in range(4): #0~3까지 돌면서 해당 번째 만에 만족시키는지
    dfs(0, 0, i)
    if result < sys.maxsize:
        break

if result >= sys.maxsize:
    print(-1)
else:
    print(result)