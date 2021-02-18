#BFS 백트래킹. Set사용에 유의.
r, c = map(int, input().split())

arr = [list(input()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

save = []
result = 1
q = set([(0, 0, arr[0][0])]) #어차피 중복 없으므로. 시간복잡도 줄이기 위해 set사용. (deque 사용시 시간초과)
while q:
    x, y, ans = q.pop() #ans : 방문한 칸들.
    for i in range(4): #BFS 탐색.
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if arr[nx][ny] not in ans: #ans에 현재칸이 없으면.
                q.add((nx, ny, ans + arr[nx][ny])) #set에 추가 및 ans 갱신.
                result = max(result, len(ans) + 1) #result값 갱신
print(result)