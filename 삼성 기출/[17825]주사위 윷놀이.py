data = list(map(int, input().split()))

board = [[i for i in range(0, 42, 2)],
         [10, 13, 16, 19, 25, 30, 35, 40],
         [20, 22, 24, 25, 30, 35, 40],
         [30, 28, 27, 26, 25, 30, 35, 40]]
pos = [[i for i in range(21)],
       [5, 21, 22, 23, 24, 25, 26, 20],
       [10, 27, 28, 24, 25, 26, 20],
       [15, 29, 30, 31, 24, 25, 26, 20]]
'''
4가지 말에 대해 주사위만큼 y를 이동.
y가 length를 넘으면 도착말로. 도착말은 점수 추가 없음.
도착말은 이동시 return 시켜 경우의 수에서 배제.
pos 따로 만듦 -> 다른 칸 같은 보드값 존재.
'''
horse = [[0, 0], [0, 0], [0, 0], [0, 0]]
result = 0
count = 0

move = [0 for _ in range(10)]

def scoring():
    global result
    horse = [[0, 0] for _ in range(4)]
    sum_val = 0
    #move: 몇번째 주사위에 몇번째말을 움직일건지 저장.
    for i in range(10):
        # i : 몇번째 주사위인지
        now = move[i] #이번에 움직일 말.
        x, y = horse[now] #그 말의 이전좌표
        if x == -1: return
        y += data[i] #주사위값
        if x == 0:
            if y >= len(board[x]): horse[now] = [-1, -1]
            elif y == 5: horse[now] = [1, 0]
            elif y == 10: horse[now] = [2, 0]
            elif y == 15: horse[now] = [3, 0]
            else: horse[now] = [x, y]
        else:
            if y >= len(board[x]): horse[now] = [-1, -1]
            else: horse[now] = [x, y]
        nx, ny = horse[now]
        if nx != -1:
            for h in range(4):
                na, nb = horse[h]
                if now == h: continue
                if na == -1: continue
                if pos[na][nb] == pos[nx][ny]: return
            sum_val += board[nx][ny]
    result = max(result, sum_val)

def dfs():
    global count
    if count == 9:
        scoring()
        return
    for i in range(4):
        count += 1
        move[count] = i
        dfs()
        count -= 1

dfs()
print(result)