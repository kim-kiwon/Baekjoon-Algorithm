#그래프 탐색. 사이클 파악.
n = int(input())

graph = [[] for _ in range(n+1)]
for i in range(n):
    graph[i+1].append(int(input()))

result = []
visited = [0] * (n+1)

def dfs(a, i): #dfs 하면서 시작지점으로 돌아오는 사이클 생기는지
    visited[a] = 1
    for b in graph[a]:
        if not(visited[b]):
            dfs(b, i)
        elif visited[b] and b == i: #사이클 생기면 해당 노드를 결과에 삽입.
            result.append(b)

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)

print(len(result))
for i in range(len(result)):
    print(result[i])
