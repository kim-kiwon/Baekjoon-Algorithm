import sys

n, k = map(int, input().split())
temp = list(map(int, input().split()))
belt = [[i, 0] for i in temp]

def can_exit():
    global k, stage
    count = 0
    for i in belt:
        if i[0] == 0:
            count += 1
    if count >= k:
        print(stage)
        sys.exit()

def down_robot():
    belt[n-1][1] = 0

stage = 0
while True:
    stage += 1
    #벨트 회전
    temp = belt[-1]
    for i in range(len(belt) - 1, 0, -1):
        belt[i] = belt[i-1]
    belt[0] = temp
    down_robot()

    #로봇 이동
    for i in range(n-1, -1, -1):
        if belt[i][1] == 1:
            if belt[i+1][1] == 0 and belt[i+1][0] > 0:
                belt[i+1][0] -= 1
                belt[i][1] = 0
                belt[i+1][1] = 1
    down_robot()

    #로봇 올리기
    if belt[0][1] == 0 and belt[0][0] != 0 :
        belt[0][1] = 1
        belt[0][0] -= 1

    can_exit()