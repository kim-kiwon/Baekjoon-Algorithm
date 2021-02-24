#이분탐색 + 올림함수

from sys import stdin
from math import ceil #올림함수 ceil

input = stdin.readline

n, m = map(int, input().split())

jewel = []
for _ in range(m):
    jewel.append(int(input()))

start, end, ans = 1, max(jewel), 0

while start <= end:
    mid = (start + end) // 2 #mid = 최대 질투심
    count = 0
    for i in jewel:
        count += ceil(i / mid)
    if count <= n: #받지 못하는 학생 있어도 되므로
        ans = mid #답 후보
        end = mid -1
    else:
        start = mid + 1

print(ans)