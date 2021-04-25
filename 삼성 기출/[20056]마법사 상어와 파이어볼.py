import copy
n, f, k = map(int, input().split())

data = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(f):
    r, c, m, s, d = map(int, input().split())
    data[r-1][c-1].append((m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    for i in range(n):
        for j in range(n):
            if len(data[i][j]) != 0:
                while data[i][j]:
                    x, y = i, j
                    m, s, d = data[i][j].pop()
                    nx = x + ((s * dx[d]) % n)
                    ny = y + ((s * dy[d]) % n)
                    if nx >= n:
                        nx %= n
                    elif nx < 0:
                        nx += n
                    if ny >= n:
                        ny %= n
                    elif ny < 0:
                        ny += n

                    temp[nx][ny].append((m, s, d))

def divide():
    for i in range(n):
        for j in range(n):
            if len(data[i][j]) >= 2:
                m_sum = 0
                s_sum = 0
                count = 0
                all_even = 1
                all_odd = 1
                for m, s, d in data[i][j]:
                    count += 1
                    m_sum += m
                    s_sum += s
                    if d % 2 == 0: all_odd = 0
                    elif d % 2 == 1: all_even = 0

                m_val = m_sum // 5
                s_val = s_sum // count
                d_val = [0, 2, 4, 6] if all_even or all_odd else [1, 3, 5, 7]

                data[i][j] = []
                if m_val == 0: continue
                for d in d_val:
                    data[i][j].append((m_val, s_val, d))

for _ in range(k):
    temp = [[[] for _ in range(n)] for _ in range(n)]
    move()
    data = copy.deepcopy(temp)
    divide()

result = 0
for i in range(n):
    for j in range(n):
        if len(data[i][j]) != 0:
            for m, s, d in data[i][j]:
                result += m

print(result)