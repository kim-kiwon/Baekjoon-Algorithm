#구현
n , l = map(int, input().split())

vals = [] #2N개의길

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n): #가로 길 삽입
    temp1 = [[0, 0] for _ in range(n)]
    for j in range(n):
        temp1[j][0] = data[i][j]
    vals.append(temp1)

for j in range(n): #세로 길 삽입
    temp1 = [[0, 0] for _ in range(n)]
    for i in range(n):
        temp1[i][0] = data[i][j]
    vals.append(temp1)

result = 0
for val in vals:
    can = 1
    for j in range(1, n):
        #현재 블록이 이전보다 크다.
        #1넘게 클때
        if val[j][0] > val[j-1][0] + 1: can = 0; break;
        #1 클때
        if val[j][0] == val[j-1][0] + 1:
            if val[j-1][1] != 0: can = 0; break; #직전 블록에 경사로 놓은 적 있으면 불가.
            prev = val[j-1][0] #직전부터 ~ 이전 l개 블록 같고. 경사로 놓은적 없는지 확인.
            for k in range(2, l+1):
                if j-k < 0 : can = 0; break;
                if val[j-k][0] != prev or val[j-k][1] != 0: can = 0; break;
                val[j-k][1] = 1
                prev = val[j-k][0]
        #현재 블록이 이전보다 작다.
        #1넘게 작을때
        if val[j][0] < val[j-1][0] - 1: can = 0; break;
        #1 작을때
        if val[j][0] == val[j-1][0] - 1:
            if val[j][1] != 0: can = 0; break; #현재 블록에 경사로 놓은적 있으면 불가.
            prev = val[j][0] #현재 블록 ~ 다음 l개 블록 같고 경사로 놓은적 없는지 확인
            val[j][1] = 1
            for k in range(1, l):
                if j + k >= n : can = 0; break;
                if val[j+k][0] != prev or val[j+k][1] != 0: can = 0; break;
                val[j+k][1] = 1
                prev = val[j+k][0]
        if can == 0: break #중간에 불가능이라 판별되면 for문 탈출.
    if can == 1: result += 1 #끝까지 가능한 것으로 판별되면 결과 추가.

print(result)