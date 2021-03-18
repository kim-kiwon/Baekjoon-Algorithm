#3차원 방문배열 이용 BFS 느낌.
#heapq 사용 최단거리만 가져옴. (n-1, n-1 방문했을때 dist 가져오기 위해)
import heapq, sys

n, t = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[[0] * 3 for _ in range(n)] for _ in range(n)]
#3차원 방문배열. 최단경로만 타고간게 목적지의 최단경로가 아니다.
#첫스텝/두스텝/세스텝에 중간방문지 거쳐서 목적지 간것 다 확인해 봐야함.

q = []
q.append((0, 0, 0, 0)) #시작점 삽입. 거리. x. y. 스텝 순서.
while q:
    dist, x, y, count = heapq.heappop(q)
    if visited[x][y][count] != 0:
        continue
    visited[x][y][count] = 1 #방문 처리
    if x == n-1 and y == n-1: #목적지 도착. 최소 힙큐 이므로 count 0 1 2 상관없이 답이 된다.
        print(dist)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            cost = dist + t
            if count == 2: #지금 밟은게 세번째 스텝.
                cost += data[nx][ny] #풀먹음
                ncount = 0
            else:
                ncount = count + 1
            heapq.heappush(q, (cost, nx, ny, ncount))