#이분탐색 + 등차수열

t = int(input())

for _ in range(t):
    n = int(input())
    start, end, ans = 0, n, 0
    while start <= end:
        mid = (start + end) // 2 #mid = 징검다리 수
        #최대한 많이 밟으려면 등차 1인 등차수열.
        #해당 등차수열 값이 n보단 작아야함.
        val = (mid) * (mid + 1) / 2
        if val <= n:
            ans = max(ans, mid)
            start = mid + 1
        else:
            end = mid - 1
    print(ans)