N = int(input())

arr = []
for i in range(N):
    s = list(map(int, input().split()))
    arr.append(s)

arr = sorted(arr, key = lambda x : (x[0], x[1]))

visit = [0 for _ in range(366)]

for i in range(N):
    for s in range(arr[i][0], arr[i][1]+1):
        visit[s-1] += 1


result = []
sumval = 0
for i in range(365):
    if visit[i] != 0:
        result.append(visit[i])
        if visit[i+1] == 0:
            sumval += max(result) * len(result)
            result = []
print(sumval)