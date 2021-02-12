#플로이드 마샬로 풀자. 모든 노드에서 모든 노드로의 최단거리 계산.
n, m = map(int, input().split())

arr = [[1e9] * (n+1) for _ in range(n+1)] #초기값 1e9로.

#자기 자신으로의 값 0으로 갱신.
for i in range(1, n):
    arr[i][i] = 0

#연결된 두 노드값 서로 1로 갱신.
for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

#플로이드 마샬 알고리즘 적용
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min((arr[a][k] + arr[k][b]), arr[a][b])

result = 1e9 #베이컨 거리 최소값.
answer = 0 #베이컨 거리가 최소가 되는 노드.
for i in range(n, 0, -1): #역순으로 확인.
    now = 0 #현재 노드에서 타 모든 노드로의 합
    for j in range(1, n+1):
        now += arr[i][j]
    result = min(now, result) #베이컨 거리 최소값 갱신
    if result == now: #갱신 되었으면 최소 노드 변경.
        answer = i #여기서 최소인 노드 나오게 하려고 역순탐지 한 것.

print(answer)