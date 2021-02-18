#행렬 다익스트라
import heapq

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

tnum = 1 #테스트 넘버
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF] * n for _ in range(n)]
    q = []
    q.append((0, 0, graph[0][0])) #시작칸 큐 삽입.
    distance[0][0] = graph[0][0]
    while q:
        x, y, dist = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4): #네 방향 탐색.
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: #이동한 칸이 지도 안이면 다익스트라로 distance 갱신.
                cost = dist + graph[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    q.append((nx, ny, cost))
    print("Problem " + str(tnum) + ": " + str(distance[n-1][n-1]))
    tnum += 1
