#플로이드 마샬
import sys
n, m = map(int, input().split())

INF = sys.maxsize
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    u, v, b = map(int, input().split())
    if b == 0:
        graph[u][v] = 0
        graph[v][u] = 1
    else:
        graph[u][v] = 0
        graph[v][u] = 0

for i in range(1, n+1):
    graph[i][i] = 0
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            dist = graph[a][k] + graph[k][b]
            if graph[a][b] > dist:
                graph[a][b] = dist

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    print(graph[a][b])


