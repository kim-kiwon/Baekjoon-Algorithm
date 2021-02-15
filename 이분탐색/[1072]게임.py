from math import floor #소수점 버림함수 floor
x, y = map(int, input().split())

start = 0
end = 1000000000

init_val = floor(100 * y / x) #초기값.

if init_val >= 99: print(-1)
else:
    while start <= end: #start = mid = end 까지 while문 진행.
        mid = (start + end) // 2
        nx, ny = x + mid, y+ mid
        if floor(100 * ny / nx) > init_val:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1) #end = mid-1 되므로 +1 하면 답 도출.
