#단순 그리디
from math import ceil
n = int(input())

arr = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0

for i in arr:
    result += 1
    i -= b
    if i > 0:
        result += ceil(i / c)

print(result)