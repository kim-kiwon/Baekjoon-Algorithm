#이분탐색
from sys import stdin

input = stdin.readline
k, n = map(int, input().split())

have = [] #갖고 있는 랜선
for _ in range(k):
    have.append(int(input()))

start = 1
end = max(have)
ans = 0

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in have: #해당 랜선의 길이가 mid 보다 크다면
        if i >= mid:
            count += (i // mid) #몫만큼 개수 증가.
    if count >= n: #개수가 목표치 이상.
        ans = mid #답 후보
        start = mid + 1
    else:
        end = mid - 1
print(ans)