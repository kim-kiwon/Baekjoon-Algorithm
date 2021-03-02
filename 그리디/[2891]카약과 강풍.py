#그리디. 항상 왼쪽 카약에 충원.
n, s, r = map(int, input().split()) #전체팀. 손상팀. 더 팀.
breaks = list(map(int, input().split()))
mores = list(map(int, input().split()))

kayaks = [0] * (n+2)

for i in range(1, n+1):
    kayaks[i] = 1

breaks.sort()
for i in breaks:
    kayaks[i] -= 1

for i in mores:
    kayaks[i] += 1

for i in breaks:
    if kayaks[i-1] >= 2:
        kayaks[i-1] -= 1
        kayaks[i] += 1
    elif kayaks[i+1] >= 2:
        kayaks[i+1] -= 1
        kayaks[i] += 1

count = 0
for i in range(1, n+1):
    if kayaks[i] == 0:
        count += 1

print(count)