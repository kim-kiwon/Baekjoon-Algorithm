import copy
n = int(input())

data = [[[0, 0] for _ in range(n)] for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        data[i][j][0] = temp[j]

def reset(): #합쳐짐 플래그 초기화
    for i in range(n):
        for j in range(n):
            data[i][j][1] = 0

def move(t): #상하좌우로 이동
    if t == 0: #위로 이동
        for j in range(n):
            for i in range(1, n):
                if data[i][j][0] != 0:
                    flag = 0
                    for k in range(i - 1, -1, -1):
                        if data[k][j][0] == data[i][j][0] and data[k][j][1] == 0:
                            data[k][j][0] *= 2
                            data[k][j][1] = 1
                            data[i][j][0] = 0
                            flag = 1
                            break
                        if data[k][j][0] != 0: break
                    if flag == 0:
                        for k in range(i-1, -2, -1):
                            if k == -1 or data[k][j][0] != 0:
                                temp = data[i][j][0]
                                data[i][j][0] = 0
                                data[k+1][j][0] = temp
                                break
    elif t == 1: #아래로 이동
        for j in range(n):
            for i in range(n - 2, -1, -1):
                if data[i][j][0] != 0:
                    flag = 0
                    for k in range(i + 1, n):
                        if data[k][j][0] == data[i][j][0] and data[k][j][1] == 0:
                            data[k][j][0] *= 2
                            data[k][j][1] = 1
                            data[i][j][0] = 0
                            flag = 1
                            break
                        if data[k][j][0] != 0: break
                    if flag == 0:
                        for k in range(i + 1, n + 1):
                            if k == n or data[k][j][0] != 0:
                                temp = data[i][j][0]
                                data[i][j][0] = 0
                                data[k - 1][j][0] = temp
                                break
    elif t == 2: #좌로 이동
        for i in range(n):
            for j in range(1, n):
                if data[i][j][0] != 0:
                    flag = 0
                    for k in range(j - 1, -1, -1):
                        if data[i][k][0] == data[i][j][0] and data[i][k][1] == 0:
                            data[i][k][0] *= 2
                            data[i][k][1] = 1
                            data[i][j][0] = 0
                            flag = 1
                            break
                        if data[i][k][0] != 0 : break
                    if flag == 0:
                        for k in range(j - 1, -2, -1):
                            if k == -1 or data[i][k][0] != 0:
                                temp = data[i][j][0]
                                data[i][j][0] = 0
                                data[i][k + 1][0] = temp
                                break
    elif t == 3: #우로 이동
        for i in range(n):
            for j in range(n-2, -1, -1):
                if data[i][j][0] != 0:
                    flag = 0
                    for k in range(j + 1, n):
                        if data[i][k][0] == data[i][j][0] and data[i][k][1] == 0:
                            data[i][k][0] *= 2
                            data[i][k][1] = 1
                            data[i][j][0] = 0
                            flag = 1
                            break
                        if data[i][k][0] != 0 : break
                    if flag == 0:
                        for k in range(j + 1, n + 1):
                            if k == n or data[i][k][0] != 0:
                                temp = data[i][j][0]
                                data[i][j][0] = 0
                                data[i][k - 1][0] = temp
                                break
    reset() #합쳐진 플래그 data[i][j][1]을 0으로 초기화

result = 0
def solve(count): #백트래킹
    global result, data
    if count == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, data[i][j][0])
        return
    temp = copy.deepcopy(data) #이동 이전 배열 상태 저장.
    for i in range(4):
        move(i) #이동시키고
        solve(count + 1) #DFS 후
        data = copy.deepcopy(temp) #원래 데이터 복구

solve(0)
print(result)