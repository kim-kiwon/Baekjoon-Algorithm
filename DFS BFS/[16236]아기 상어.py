#BFS + minheap (heapq)

from collections import deque
import heapq

n = int(input())
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    arr.append(temp)
    for j in range(n):
        if temp[j] == 9:
            shark = [i, j] # 상어좌표 shark
            arr[i][j] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    global shark_size
    can_fish = [] #먹을 수 있는 물고기 list. 거리
    q = deque()
    q.append((x, y))
    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: #인접좌표 이동하면서
                if arr[nx][ny] <= shark_size and visited[nx][ny] == 0: #방문 할 수 있는곳 : visited 거리로 갱신 + 큐삽입
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if arr[nx][ny] < shark_size and arr[nx][ny] != 0: #먹을 수 있는 물고기 : can_fish에 거리와 좌표 삽입.
                        heapq.heappush(can_fish, (visited[nx][ny] - 1, nx, ny))
    return can_fish #can_fish 반환.

shark_size = 2
eat_count = 0
result = 0
while True:
    can_fish = bfs(shark[0], shark[1])
    if len(can_fish) == 0: #먹을 수 있는 물고기 없으면 종료
        break
    dist, fishx, fishy = heapq.heappop(can_fish) #먹을 수 있는 물고기 중 가장 가까운 물고기.
    result += dist # result 갱신
    arr[fishx][fishy] = 0 #먹은 물고기 없애기.

    #상어 좌표 이동
    shark[0] = fishx
    shark[1] = fishy

    #먹은 물고기 양이 상어크기와 같다면 상어크기 갱신
    eat_count += 1
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(result)