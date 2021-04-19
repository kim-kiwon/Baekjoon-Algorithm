n = int(input())
data = list(map(int, input().split()))

data.sort()
if n % 2 == 1:
    a = data[(n-1)//2]
    print(a)
else:
    a = data[(n-1)//2]
    b = data[(n-1)//2 + 1]
    a_val, b_val = 0, 0
    for i in data:
        a_val += abs(i - a)
        b_val += abs(i - b)
    if b_val < a_val:
        print(b)
    else:
        print(a)