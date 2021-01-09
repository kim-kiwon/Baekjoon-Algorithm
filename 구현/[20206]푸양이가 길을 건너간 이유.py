A, B, C = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())

flag = 0

if A == 0:
    yval = (-C/B)
    if yval > y1 and yval < y2:
        flag = 1
elif B == 0:
    xval = (-C / A)
    if xval > x1 and xval < x2:
        flag = 1
else:
    for x in range(x1, x2 + 1):
        y = (-(A * x) - C) / B
        if y > y1 and y < y2:
            flag = 1
            break

if flag == 0:
    print("Lucky")
else:
    print("Poor")