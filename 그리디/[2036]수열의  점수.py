#그리디

n = int(input())
plus, zeros, minus = [], [], [] #양수. 0. 음수 따로 받음.
for i in range(n):
    a = int(input())
    if a > 0:
        plus.append(a)
    elif a == 0:
        zeros.append(a)
    else:
        minus.append(a)


result = 0

#양수 처리
plus.sort()
while True: #큰수 부터 빼서 곱으로 더해주다가. 1이나오면 탈출.
    if len(plus) <= 1: break
    a = plus.pop()
    b = plus.pop()
    if a == 1 or b == 1:
        plus.append(a)
        plus.append(b)
        break
    result += a * b

while plus: #남은 양수와 1들 처리.
    a = plus.pop()
    result += a

#음수 처리
minus.sort(reverse=True)
while True: #음수 하나 남을때 까지 곱으로 더해줌.
    if len(minus) <= 1: break
    a = minus.pop()
    b = minus.pop()
    result += a * b

if len(zeros) == 0 and len(minus) != 0: #음수가 남고. 0이 없으면 결과에 더해줌.
                                        #나머지 경우 0 으로 상쇄.
    result += minus.pop()

print(result)