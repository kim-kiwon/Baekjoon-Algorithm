#증가하는 부분수열과 같은 문제.
n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n): #dp[i] 채우기.
    for j in range(0, i): #앞의 원소와 비교하여
        if arr[j] < arr[i]: #앞의 원소가 더 작으면
            dp[i] = max(dp[i], dp[j] + 1) #해당 dp값+1 한 것중 가장 큰값.

print(max(dp))