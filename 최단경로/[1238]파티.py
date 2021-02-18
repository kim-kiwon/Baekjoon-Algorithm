#다익스트라.
#플로이드 와샬 시간복잡도 = N^3 = 10억이되므로 시간초과.
import heapq

INF = int(1e9)

n, m ,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, t, c = map(int, input().split())
    graph[s].append((t, c))

# x->모든 집    으로 돌아가는 경로 먼저 distance에 저장.
distance = [INF] * (n+1)
q = []
q.append((x, 0))
distance[x] = 0
while q:
    now, dist = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (i[0], cost))

#각 노드(i) 에서 x로 가는 cost. distance[i]에 더해줌.
for i in range(1, n+1):
    if i != x:
        temp_distance = [INF] * (n + 1)
        q = []
        q.append((i, 0))
        temp_distance[i] = 0
        while q:
            now, dist = heapq.heappop(q)
            if dist > temp_distance[now]:
                continue
            for j in graph[now]:
                cost = dist + j[1]
                if cost < temp_distance[j[0]]:
                    temp_distance[j[0]] = cost
                    heapq.heappush(q, (j[0], cost))
        distance[i] += temp_distance[x]
#여기까지 수행하면 distance에는 각 노드 -> x로 왕복 최단경로의 합이 저장되어있음.

#0이 INF라 최대값 되므로 음수로 변경.
distance[0] = -int(1e9)

print(max(distance))