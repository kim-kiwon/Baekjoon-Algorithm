#벽 부수는 수 = 비용으로 치면 행렬 다익스트라 문제.
import heapq, sys
m, n = map(int, input().split())

INF = sys.maxsize
data = []
for _ in range(n):
    temp = list(map(int, list(input())))
    data.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

distance = [[INF] * m for _ in range(n)]
distance[0][0] = 0
q = []
q.append((0, 0, 0)) #비용. x. y
while q:
    dist, x, y = heapq.heappop(q)
    if dist > distance[x][y]:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < m:
            cost = dist + data[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
print(distance[n-1][m-1])