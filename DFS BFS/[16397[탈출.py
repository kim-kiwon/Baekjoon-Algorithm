#BFS
#1. t 초과하는 경우 ->ANG
#2. g 찾는 경우 -> 횟수 출력
#3. 큐 빌때까지 못찾는 경우 ->ANG

from collections import deque

n, t, g = map(int, input().split()) #n: 처음수. T: 최대수. G:탈출넘버

visited = [0] * 100000
def button_a(n):
    return n + 1

def button_b(n):
    n *= 2
    if n != 0:
        n = str(n)
        for i in range(len(n)):
            if n[i] != '0':
                n = n[:i] + str(int(n[i]) - 1) + n[i+1:]
                n = int(n)
                break
    return n

q = deque()
q.append(n)
visited[n] = 1
flag = 0 #큐 빌때까지 못찾는 경우 예외처리 위한 플래그
while q:
    val = q.popleft()
    if visited[val] - 1 > t:
        print("ANG")
        flag = 1
        break
    if val == g:
        print(visited[val] - 1)
        flag = 1
        break
    val_a = button_a(val)
    val_b = button_b(val)
    if val + 1 <= 99999 and visited[val_a] == 0:
        q.append(val_a)
        visited[val_a] = visited[val] + 1
    if val * 2 <= 99999 and visited[val_b] == 0:
        q.append(val_b)
        visited[val_b] = visited[val] + 1

if flag == 0:
    print("ANG")