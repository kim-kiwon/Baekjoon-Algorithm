N, K = map(int, input().split())

arr = []
[arr.append(list(map(int, input().split()))) for _ in range(N)]

result = [[0 for _ in range(N*K)] for _ in range(N*K)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            for q in range(K):
                for w in range(K):
                    result[i*K+q][j*K+w] = 1
for i in range(N*K):
    print(*result[i])