n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
#[i][0]은 i번째 집을 빨간색으로 칠할 경우 최소값.
print(min(arr[n-1]))