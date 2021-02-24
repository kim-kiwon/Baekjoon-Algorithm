#dfs 진행하여 개수 세기.

t = int(input())

def dfs(j):
    if visited[j] == 1:
        return False
    else:
        visited[j] = 1
        dfs(arr[j])
        return True
for i in range(t):
    n = int(input())
    visited = [0] * (n+1)
    arr = [0] + list(map(int, input().split()))
    count = 0
    for j in range(1, n+1):
        if dfs(j) == True:
            count += 1
    print(count)