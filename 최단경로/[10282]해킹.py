#다익스트라.
import heapq

INF = int(1e9)

def dijkstra(start, n):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                q.append((i[0], cost))
    return distance

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split()) #a가 b를 의존. b가 감염되면 a가 감염됨.
        graph[b].append((a, s)) #b에서 a로 갈수있도록 b 그래프에 삽입.
    distval = dijkstra(c, n) #c에서 시작. n 개 노드. 다익스트라 distance 리스트.
    count = 0 #감염된 수
    max_val = -1e9 #감염된 노드 중 최대 거리
    for i in range(1, n+1): #모든 노드 검사
        if distval[i] < INF: #해당 노드가 감염되었다면
            count += 1 #개수 증가
            max_val = max(max_val, distval[i]) #최대 거리 갱신
    print(count, max_val, end = " ")