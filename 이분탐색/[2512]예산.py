#이분탐색

n = int(input())

request = list(map(int, input().split()))

m = int(input())

start, end = 0, max(request)
ans = 0
while start <= end:
    mid = (start + end) // 2
    sum_val = 0
    for i in request:
        if i <= mid:
            sum_val += i
        else:
            sum_val += mid
    if sum_val > m:
        end = mid -1
    else:
        ans = mid #답 후보
        start = mid + 1

print(ans)