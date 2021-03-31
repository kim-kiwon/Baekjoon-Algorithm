#구현 + 시뮬레이션

#네개 톱니
top1 = list(map(int, list(input())))
top2 = list(map(int, list(input())))
top3 = list(map(int, list(input())))
top4 = list(map(int, list(input())))

#시계방향, 반시계방향 회전함수
def rotate(topni, direc):
    if direc == 1:
        temp = topni[7]
        for i in range(7, 0, -1):
            topni[i] = topni[i - 1]
        topni[0] = temp
    elif direc == -1:
        temp = topni[0]
        for i in range(7):
            topni[i] = topni[i + 1]
        topni[7] = temp



k = int(input())
for _ in range(k):
    num, direc = map(int, input().split())
    #입력 조건에따라 시계방향, 반시계방향, 회전X 정해주기
    r1, r2, r3, r4 = 0, 0, 0, 0
    if num == 1:
        r1 = direc
        if top1[2] != top2[6]:
            r2 = -r1
        if top2[2] != top3[6]:
            r3 = -r2
        if top3[2] != top4[6]:
            r4 = -r3
    elif num == 2:
        r2 = direc
        if top1[2] != top2[6]:
            r1 = -r2
        if top2[2] != top3[6]:
            r3 = -r2
        if top3[2] != top4[6]:
            r4 = -r3
    elif num == 3:
        r3 = direc
        if top3[2] != top4[6]:
            r4 = -r3
        if top2[2] != top3[6]:
            r2 = -r3
        if top1[2] != top2[6]:
            r1 = -r2
    elif num == 4:
        r4 = direc
        if top3[2] != top4[6]:
            r3 = -r4
        if top2[2] != top3[6]:
            r2 = -r3
        if top1[2] != top2[6]:
            r1 = -r2
    #네개 톱니 회전
    rotate(top1, r1)
    rotate(top2, r2)
    rotate(top3, r3)
    rotate(top4, r4)

#결과 출력
result = 0
if top1[0] == 1:
    result += 1
if top2[0] == 1:
    result += 2
if top3[0] == 1:
    result += 4
if top4[0] == 1:
    result += 8

print(result)
