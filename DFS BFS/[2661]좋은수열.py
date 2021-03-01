#백트래킹 DFS
n = int(input())

arr = []

def dfs(idx):
    for i in range(1, (idx//2) + 1):
        if arr[-i:] == arr[-2*i:-i]:
            return -1
    if idx == n:
        for i in range(n):
            print(arr[i], end ='')
        return 0
    for i in range(1, 4):
        arr.append(i)
        if dfs(idx + 1) == 0: #가장 먼저 출력되는것 출력하고
            return 0 #함수 종료. 즉 최소값만 출력하게됨.
        arr.pop()

dfs(0)