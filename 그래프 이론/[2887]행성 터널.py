#위상정렬
from collections import deque

t = int(input())

for _ in range(t): #테스트 수
    n = int(input()) #노드 수
    last_year = list(map(int, input().split())) #작년 결과
    len_ly = len(last_year)
    graph = [[] for _ in range(n+1)] #graph[i] : i번째 노드보다 순위가 낮은 노드들.
    indegree = [0] * (n+1) #방문 차수
    for i in range(len_ly): #i번째 노드보다 순위 낮은 노드들 graph[i]에 삽입 및 삽입된 노드들 방문 차수 증가.
        for j in range(-len_ly + 1 + i, 0):
            graph[last_year[i]].append(last_year[j])
            indegree[last_year[j]] += 1
    m = int(input()) #변경 수
    for _ in range(m):
        a, b = map(int, input().split()) #변경된 두 노드
        if a in graph[b]: # b -> a 순서라면.
            graph[b].remove(a)
            graph[a].append(b)
            indegree[a] -= 1
            indegree[b] += 1 #a->b로 변경.
        else: # a -> b 순서라면 b -> a 로 변경.
            graph[a].remove(b)
            graph[b].append(a)
            indegree[b] -= 1
            indegree[a] += 1
    result = [] #위상정렬 결과
    q = deque()
    for i in range(1, n+1): #방문차수 0 큐에 삽입.
        if indegree[i] == 0:
            q.append(i)

    #사이클과 위상정렬 여러개 검출 위한 flag들.
    cycle = False
    only_one = True
    for i in range(n): #위상정렬이므로 n번 반복하면 n개 정렬됨.
        if len(q) == 0: #도중 q가 비면 -> 노드끼리 사이클 존재.
            cycle = True
            break
        elif len(q) >= 2: #도중 q가 여러개 -> 위상정렬 가지 수가 여러개가 됨.
            only_one = False
            break
        now = q.popleft()
        result.append(now)
        #위상정렬 수행.
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    #Flag에 따른 결과 출력
    if cycle:
        print("IMPOSSIBLE")
    elif not only_one:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()