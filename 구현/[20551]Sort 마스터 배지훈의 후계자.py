n, m = map(int, input().split())

arr = []
query = []

for _ in range(n):
    arr.append(int(input()))

for i in range(m):
    query.append([int(input()), i])

arr.sort()
query.sort()

i = j = 0
while 1:
    if i == m:
        break
    if j == n:
        for k in range(i, m):
            query[k][0] = -1
        break
    if query[i][0] == arr[j]:
        query[i][0] = j
        i += 1
    elif query[i][0] > arr[j]:
        j += 1
    else:
        query[i][0] = -1
        i += 1

query.sort(key = lambda x : x[1])

for i in range(m):
    print(query[i][0])