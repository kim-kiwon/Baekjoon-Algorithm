#BFS

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    conv = []
    for i in range(n):
        x, y = map(int, input().split())
        conv.append((x,y))
    dx, dy = map(int, input().split())

    result = "sad"
    visited = [0 for _ in range(n)]
    q = deque()
    q.append([sx, sy])
    while q:
        x, y = q.popleft()
        if abs(x - dx) + abs(y - dy) <= 1000:
            result = "happy"
            break
        for i in range(n):
            if visited[i] == 1 or abs(x - conv[i][0]) + abs(y - conv[i][1]) > 1000:
                continue
            q.append((conv[i][0], conv[i][1]))
            visited[i] = 1
    print(result)