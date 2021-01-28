N = int(input())
arr = [input().split() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] in ["+", "-", "*"]:
            continue
        arr[i][j] = int(arr[i][j])

maxval = -100000000
minval = 100000000

def dfs2(r, c, num, sign, count):
    global maxval,minval
    if r == 0 and c == 0: #밟은게 첫칸
        newnum = arr[r][c]
        newsign = sign
    elif count % 2 == 0: #밟은게 숫자
        if sign == '*':
            newnum = num * arr[r][c]
        elif sign == '+':
            newnum = num + arr[r][c]
        elif sign == '-':
            newnum = num - arr[r][c]
        if r == N - 1 and c == N - 1: #밟은게 마지막칸
            maxval = max(maxval, newnum)
            minval = min(minval, newnum)
            return
        newsign = sign
    elif count % 2 == 1: #밟은게 기호
        newsign = arr[r][c]
        newnum = num
    if r + 1 <= N-1:
        dfs2(r + 1, c, newnum, newsign, count + 1)
    if c + 1 <= N-1:
        dfs2(r, c + 1, newnum, newsign, count + 1)

dfs2(0, 0, 0, 0, 0)
print(maxval, minval)