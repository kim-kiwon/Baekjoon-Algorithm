n = int(input())

blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

def put(c, t, x, y):
    if c == 0: #green
        have = 0
        if t == 1 or t == 3:
            for i in range(6):
                if green[i][y] == 1:
                    have = 1
                    break
            if have == 1: x = i - 1
            else: x = 5
            green[x][y] = 1
            if t == 3:
                green[x-1][y] = 1
        elif t == 2:
            for i in range(6):
                if green[i][y] == 1 or green[i][y+1] == 1:
                    have = 1
                    break
            if have == 1: x = i - 1
            else: x = 5
            green[x][y] = 1
            green[x][y+1] = 1
    elif c == 1: #blue
        have = 0
        if t == 1 or t == 2:
            for i in range(6):
                if blue[x][i] == 1:
                    have = 1
                    break
            if have == 1: y = i - 1
            else : y = 5
            blue[x][y] = 1
            if t == 2:
                blue[x][y-1] = 1
        elif t == 3:
            for i in range(6):
                if blue[x][i] == 1 or blue[x+1][i] == 1:
                    have = 1
                    break
            if have == 1: y = i - 1
            else: y = 5
            blue[x][y] = 1
            blue[x+1][y] = 1

def get_score():
    global blue, score, green
    blue = list(map(list, zip(*blue)))
    for i in range(2, 6):
        if sum(green[i]) == 4:
            for a in range(i, -1, -1):
                if a == 0:
                    green[a] = [0, 0, 0, 0]
                    break
                green[a] = green[a-1]
            score += 1
        if sum(blue[i]) == 4:
            for a in range(i, -1, -1):
                if a == 0:
                    blue[a] = [0, 0, 0, 0]
                    break
                blue[a] = blue[a-1]
            score += 1
    blue = list(map(list, zip(*blue)))

def special_block():
    global green, blue
    blue = list(map(list, zip(*blue)))
    for i in range(2):
        if sum(green[i]) != 0:
            for a in range(5, -1, -1):
                if a == 0:
                    green[a] = [0, 0, 0, 0]
                    break
                green[a] = green[a-1]
        if sum(blue[i]) != 0:
            for a in range(5, -1, -1):
                if a == 0:
                    blue[a] = [0, 0, 0, 0]
                    break
                blue[a] = blue[a-1]
    blue = list(map(list, zip(*blue)))

def counting():
    result = 0
    for i in range(2, 6):
        for j in range(4):
            if green[i][j] == 1:
                result += 1
    for i in range(4):
        for j in range(2, 6):
            if blue[i][j] == 1:
                result += 1
    return result
def show():
    print("Green")
    for i in range(6):
        print(green[i])
    print()
    print("blue")
    for i in range(4):
        print(blue[i])

score = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    put(0, t, x, y)
    put(1, t, x, y)
    get_score()
    special_block()

print(score)
print(counting())