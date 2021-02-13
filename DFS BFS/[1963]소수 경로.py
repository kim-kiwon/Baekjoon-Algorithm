#에라토스테네스의 체 사용 (원래 범위의 소수를 구할때 사용함)

from collections import deque
from sys import stdin
prime = [True] * 10000 # 0~9999 모두 소수로 간주.
for i in range(2, 101): #제곱근까지 검사.
    if prime[i] == 1: #해당 수가 소수면.
        for j in range(i+i, 10000, i): #해당 수 배수를 모두 소수 False로
            prime[j] = False

def bfs(src, dest):
    q = deque()
    q.append((src, 0))
    while q:
        val, count = q.popleft()
        if val == dest:
            return count
        str_val = str(val)
        for i in range(4):
            for j in map(str, range(10)):
                if i == 0 and j == '0': #첫자리가 0이되면 제외
                    continue
                num = int(str_val[:i] + j + str_val[i+1:]) #슬라이싱 활용 변경
                if prime[num] and not visited[num]: #변경한 수가 소수이며. 방문한 적 없으면 큐에 추가
                    visited[num] = 1
                    q.append((num, count+1))
    return("Impossible")

t = int(input())
for _ in range(t):
    visited = [0] * 10000
    src, dest = map(int, input().split())
    print(bfs(src, dest))