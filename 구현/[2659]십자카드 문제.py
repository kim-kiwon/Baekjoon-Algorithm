def find_cross_num(val): #시계수 반환함수
    cross_num = val
    for _ in range(3):
        val = (val % 1000) * 10 + (val // 1000)
        if val < cross_num:
            cross_num = val
    return cross_num

cross_num = find_cross_num(int("".join(input().split())))

count = 0
check = 1111
while(check <= cross_num):
    if find_cross_num(check) == check: #처음 등장한 시계수라면.
        count += 1 #카운트 증가.
    check += 1 #체크값 계속 증가시켜나감.

print(count)