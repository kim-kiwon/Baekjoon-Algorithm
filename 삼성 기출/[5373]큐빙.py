from collections import deque

cube = [[[0]* 3 for _ in range(3)] for _ in range(6)]

def init():
    global cube
    cube = [[['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']], #상
            [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']], #앞
            [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']], #좌
            [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']], #우
            [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], #밑
            [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]] #뒤

def c_rotate(arr):
    ret_arr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ret_arr[i][j] = arr[2-j][i]
    return ret_arr

def ac_rotate(arr):
    ret_arr = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ret_arr[i][j] = arr[j][2-i]
    return ret_arr

t = int(input())
for _ in range(t):
    init()
    n = int(input())
    data = deque(list(input().split()))
    while data:
        val = data.popleft()
        if val[0] == 'U':
            if val[1] == '+':
                cube[5][0], cube[3][0], cube[1][0], cube[2][0] = cube[2][0], cube[5][0], cube[3][0], cube[1][0]
                cube[0] = c_rotate(cube[0])
            elif val[1] == '-':
                cube[5][0], cube[3][0], cube[1][0], cube[2][0] = cube[3][0], cube[1][0], cube[2][0], cube[5][0]
                cube[0] = ac_rotate(cube[0])
        elif val[0] == 'F':
            if val[1] == '+':
                temp1, temp2, temp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
                cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
                cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
                cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
                cube[3][0][0], cube[3][1][0], cube[3][2][0] = temp1, temp2, temp3
                cube[1] = c_rotate(cube[1])
            elif val[1] == '-':
                temp1, temp2, temp3 = cube[0][2][0], cube[0][2][1], cube[0][2][2]
                cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
                cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[4][0][2], cube[4][0][1], cube[4][0][0]
                cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
                cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp3, temp2, temp1
                cube[1] = ac_rotate(cube[1])
        elif val[0] == 'L':
            if val[1] == '+':
                temp1, temp2, temp3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
                cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
                cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
                cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
                cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp1, temp2, temp3
                cube[2] = c_rotate(cube[2])
            elif val[1] == '-':
                temp1, temp2, temp3 = cube[0][0][0], cube[0][1][0], cube[0][2][0]
                cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
                cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[4][0][0], cube[4][1][0], cube[4][2][0]
                cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
                cube[5][0][2], cube[5][1][2], cube[5][2][2] = temp3, temp2, temp1
                cube[2] = ac_rotate(cube[2])
        elif val[0] == 'R':
            if val[1] == '+':
                temp1, temp2, temp3 = cube[1][0][2], cube[1][1][2], cube[1][2][2]
                cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[4][0][2], cube[4][1][2], cube[4][2][2]
                cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
                cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[0][2][2], cube[0][1][2], cube[0][0][2]
                cube[0][0][2], cube[0][1][2], cube[0][2][2] = temp1, temp2, temp3
                cube[3] = c_rotate(cube[3])
            elif val[1] == '-':
                temp1, temp2, temp3 = cube[1][0][2], cube[1][1][2], cube[1][2][2]
                cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[0][0][2], cube[0][1][2], cube[0][2][2]
                cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
                cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
                cube[4][0][2], cube[4][1][2], cube[4][2][2] = temp1, temp2, temp3
                cube[3] = ac_rotate(cube[3])
        elif val[0] == 'D':
            if val[1] == '+':
                cube[1][2], cube[3][2], cube[5][2], cube[2][2] = cube[2][2], cube[1][2], cube[3][2], cube[5][2]
                cube[4] = c_rotate(cube[4])
            elif val[1] == '-':
                cube[1][2], cube[3][2], cube[5][2], cube[2][2] = cube[3][2], cube[5][2], cube[2][2], cube[1][2]
                cube[4] = ac_rotate(cube[4])
        elif val[0] == 'B':
            if val[1] == '+':
                temp1, temp2, temp3 = cube[3][0][2], cube[3][1][2], cube[3][2][2]
                cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[4][2][2], cube[4][2][1], cube[4][2][0]
                cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
                cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
                cube[0][0][0], cube[0][0][1], cube[0][0][2] = temp1, temp2, temp3
                cube[5] = c_rotate(cube[5])
            elif val[1] == '-':
                temp1, temp2, temp3 = cube[3][0][2], cube[3][1][2], cube[3][2][2]
                cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[0][0][0], cube[0][0][1], cube[0][0][2]
                cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
                cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
                cube[4][2][0], cube[4][2][1], cube[4][2][2] = temp3, temp2, temp1
                cube[5] = ac_rotate(cube[5])
    for i in range(3):
        result = ''.join(cube[0][i])
        print(result)