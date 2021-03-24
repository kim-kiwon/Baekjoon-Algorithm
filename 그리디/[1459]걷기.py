x, y, w, s=map(int, input().split())
a = (x + y) * w
b = min(x, y) * s + (x + y - min(x, y) * 2)*w
if (x + y) % 2 == 0 :
    c = s * max(x, y)
else:
    c = s * (max(x, y) - 1) + w
print(min(a, b, c))