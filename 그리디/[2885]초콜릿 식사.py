#그리디. 큰 덩어리부터 선택.
#쪼갤때만 카운트 증가.
k = int(input())

val = 1

while True:
    if val >= k:
        break
    else:
        val *= 2

count = 0
size = val
while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1
print(val, count)