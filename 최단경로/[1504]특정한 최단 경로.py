#다익스트라 여러번
import heapq
INF = int(1e9)

n, e = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost)) #그래프 양방향 삽입.
    graph[b].append((a, cost))

d1, d2 = map(int, input().split()) #경유지1, 경유지2

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance #거리 리스트 반환

dis1 = dijkstra(1)
dis2 = dijkstra(d1)
dis3 = dijkstra(d2)

result1 = dis1[d1] + dis2[d2] + dis3[n] #1 -> d1 -> d2 -> n
result2 = dis1[d2] + dis3[d1] + dis2[n] #1 -> d2 -> d1 -> n

if result1 >= INF and result2 >= INF: #두 경로 모두 도달 불가능시
    print(-1)
else:
    print(min(result1, result2))