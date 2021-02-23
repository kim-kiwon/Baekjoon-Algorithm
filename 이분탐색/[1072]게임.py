from math import floor #소수점 버림함수 floor
x, y = map(int, input().split())

first_val = floor(100 * y / x )

ans = -1 #답 초기값 -1. 한번도 갱신 안되면 -1로 출력.
start = 1
end =  1000000000
while start <= end:
    mid = (start + end) // 2
    val = floor(100 * (y+mid) / (x+mid)) #mid만큼 진행한 승률
    if val >= first_val + 1: #해당 승률이 처음값보다 크다면.
        ans = mid #답 갱신.
        end = mid - 1
    else:
        start = mid + 1
print(ans)
