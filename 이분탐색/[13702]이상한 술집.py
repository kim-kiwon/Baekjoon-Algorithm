#이분탐색
n, k = map(int, input().split())

mak = []
for _ in range(n):
    mak.append(int(input()))

answer = 0

start, end = 0, max(mak)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in mak:
        if i >= mid:
            count += (i // mid)
    if count >= k:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)