#이분탐색 or math 라이브러리 활용

n = int(input())
start, end = 0, 2**63
answer = 0
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 >= n:
        answer = mid
        end = mid -1
    else:
        start = mid + 1

print(answer)