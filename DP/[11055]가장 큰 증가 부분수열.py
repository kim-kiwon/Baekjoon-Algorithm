N = int(input())
arr = [0] + list(map(int, input().split()))
DP = [0 for _ in range(N+1)]
for i in range(N+1):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(DP[i], DP[j]+arr[i])
print(max(DP))
