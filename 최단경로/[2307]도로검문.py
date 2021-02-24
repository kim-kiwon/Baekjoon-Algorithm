#다익스트라 + 경로추적
import heapq

n, m = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(n+1)]

previous = [1] * (n+1) #이전 노드 저장

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))


def dijkstra():
    distance = [INF] * (n+1)
    distance[1] = 0
    q = []
    q.append((1, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
                previous[i[0]] = now
    return distance[n]

init_val = dijkstra() #다익스트라 수행. 초기 최단경로 저장.
temp = [] #1->n 까지 최단경로에 거치는 간선들 저장할 리스트.
now = n #n부터 1까지 역순으로 탐지할것.
while True:
    if now == 1: break #1까지 탐지 완료시 종료
    a = previous[now] #a : 이전노드
    b = now #b : 현재노드
    for i in graph[now]: #dist = 이전노드 -> 현재노드 거리.
        if i[0] == previous[now]:
            dist = i[1]
            break
    temp.append((a, b, dist)) #temp에 이전노드 현재노드 거리 삽입.
    now = previous[now]

max_val = -1e9

#최단경로에 사용하는 간선들 없애는게 아니면
#반드시 최단경로 사용할 것이기에 cost변화 없다.
while True:
    if len(temp) == 0: break
    #최단경로에 사용한 간선 중 하나 삭제 -> 다익스트라로 거리측정 -> 다시 추가
    a, b, dist = temp.pop()
    graph[a].remove((b, dist))
    graph[b].remove((a, dist))
    max_val = max(max_val, dijkstra())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

if max_val >= 1e9:
    print(-1)
else:
    print(max_val - init_val)