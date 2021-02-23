#이분탐색.
n, m = map(int, input().split())

arr = list(map(int, input().split()))

start, end = 1, max(arr)
ans = 0
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in arr: #나무 값 돌면서 자른길이 result에 더해줌.
        if i >= mid:
            result += (i - mid)
    if result >= m: #목표치보다 result가 더 크면.
        ans = mid #답 후보.
        start = mid + 1
    else:
        end = mid - 1
print(ans)