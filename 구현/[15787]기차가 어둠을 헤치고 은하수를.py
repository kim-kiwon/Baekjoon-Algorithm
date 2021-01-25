N, M = map(int, input().split())

train = []
for _ in range(N):
    train.append([0 for _ in range(20)])

#train[N][20] 생성.

for i in range(M):
    order = list(map(int , input().split()));
    #order[0] :무슨명령. order[1]: 대상기차. order[2]: 칸
    if order[0] == 1:
        train[order[1]-1][order[2]-1] = 1
    elif order[0] == 2:
        train[order[1]-1][order[2]-1] = 0
    elif order[0] == 3:
        for j in range(18, -1, -1):
            train[order[1]-1][j+1] = train[order[1]-1][j]
        train[order[1] - 1][0] = 0
    elif order[0] == 4:
        for j in range(1, 20):
            train[order[1]-1][j-1] = train[order[1]-1][j]
        train[order[1] - 1][19] = 0

result = []
for i in range(N):
    if train[i] not in result:
        result.append(train[i])

print(len(result))