'''
1. 같은 값일 경우 집합에 저장 후에 일괄처리 (선처리 하면 이로 인해 같아지는 값 생김)
2. 모든 값이 0일 경우 zero_division 발생. 예외처리 해줄것.
'''
n, m, t = map(int, input().split())

data = []

def c_rotate(arr, count):
    for _ in range(count):
        temp = arr[0]
        arr[0] = arr[len(arr) - 1]
        for i in range(len(arr) - 1, 1, -1):
            arr[i] = arr[i-1]
        arr[1] = temp

def ac_rotate(arr, count):
    for _ in range(count):
        temp = arr[0]
        for i in range(0, len(arr) - 1):
            arr[i] = arr[i+1]
        arr[len(arr) - 1] = temp

for _ in range(n):
    data.append(list(map(int, input().split())))

for _ in range(t):
    x, d, k = map(int, input().split())
    for i in range(x - 1, n, x):
        if d == 0:
            c_rotate(data[i], k)
        else:
            ac_rotate(data[i], k)
    sum_val = 0
    count_val = 0
    not_0 = set()
    friend = set()
    for i in range(n):
        if data[i][0] != 0 and data[i][0] == data[i][m-1]:
            friend.add((i, 0))
            friend.add((i, m-1))
        for j in range(m):
            if data[i][j] != 0: sum_val += data[i][j]; count_val += 1; not_0.add((i, j))
            if data[i][j] == 0: continue
            if j - 1 > 0 and data[i][j] == data[i][j-1]:
                friend.add((i, j))
                friend.add((i, j-1))
            if j + 1 < m and data[i][j] == data[i][j+1]:
                friend.add((i, j))
                friend.add((i, j+1))
            if i - 1 > 0 and data[i][j] == data[i-1][j]:
                friend.add((i, j))
                friend.add((i - 1, j))
            if i + 1 < n and data[i][j] == data[i+1][j]:
                friend.add((i, j))
                friend.add((i + 1, j))

    if len(friend) != 0:
        for x, y in friend:
            data[x][y] = 0
    elif sum_val == 0:
        break
    else:
        avg_val = sum_val / count_val
        for x, y in not_0:
            if data[x][y] > avg_val:
                data[x][y] -= 1
            elif data[x][y] < avg_val:
                data[x][y] += 1


result = 0
for i in range(n):
    result += sum(data[i])

print(result)