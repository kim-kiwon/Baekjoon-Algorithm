#특정 범위 숫자 bfs탐색 문제
from collections import deque

def bfs(a):
    global b
    q= deque()
    q.append((a, ""))
    while q:
        num, result = q.popleft()

        #b 찾을 경우
        if num == b:
            return result #경로문자 return

        #D연산
        dval = (2 * num) % 10000
        if visited[dval] == 0:
            visited[dval] = 1
            q.append((dval, result+"D"))

        #S연산
        sval = num - 1 if num != 0 else 9999
        if visited[sval] == 0:
            visited[sval] = 1
            q.append((sval, result+"S"))

        #L연산
        lval = int(num % 1000 * 10 + num / 1000)
        if visited[lval] == 0:
            visited[lval] = 1
            q.append((lval, result +"L"))

        #R연산
        rval = int(num % 10 * 1000 + num // 10)
        if visited[rval] == 0:
            visited[rval] = 1
            q.append((rval, result+"R"))

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    visited = [0] * 10001
    print(bfs(a))