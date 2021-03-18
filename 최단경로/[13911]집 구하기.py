#여러 지점으로부터 다익스트라. 더미노드의 도입
import heapq, sys
INF = sys.maxsize
v, e = map(int, input().split())

graph = [[] for _ in range(v+3)]
#v+1 : 모든 맥도날드 지점과 거리 0인 더미 노드
#v+2 : 모든 스타벅스 지점과 거리 0인 더미 노드
for i in range(e):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

m, x = map(int, input().split())
macs = list(map(int, input().split()))

#맥도날드 더미노드와 맥도날드 노드들 연결
for mac in macs:
    graph[v+1].append((mac, 0))
    graph[mac].append((v+1, 0))

s, y = map(int, input().split())
stars = list(map(int, input().split()))

#스타벅스 더미노드와 스타벅드 노드들 연결
for star in stars:
    graph[v+2].append((star, 0))
    graph[star].append((v+2, 0))

#다익스트라
def dijkstra(start):
    distance = [INF] * (v+3)
    q = []
    q.append((0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if i[0] == v + 1 or i[0] == v + 2:
                continue #더미노드 거쳐가는 경우 제외.(큐에 삽입 안되게)
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

result = [[] for _ in range(v+3)]

mac_val = dijkstra(v+1) #맥도날드 더미 기준 다익스트라
star_val = dijkstra(v+2) #스타벅스 더미 기준 다익스트라

for i in range(v+1): #모든 노드 결과에 삽입
    result[i].append(mac_val[i])
    result[i].append(star_val[i])

result.sort(key = lambda x : (x[0] + x[1])) #합 기준 정렬

for i in result:
    if i[0] == 0 or i[1] == 0: #둘 중 하나가 0 : 집이 아니고 맥도날드거나 스타벅스임
        continue
    if i[0] <= x and i[1] <= y: #만족 결과 있으면 출력 후 종료
        print(i[0] + i[1])
        sys.exit()

print(-1)