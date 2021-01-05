from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

sum = [arr[0]]
for i in range(len(arr) - 1):
    sum.append(max(sum[i] + arr[i + 1], arr[i + 1]))
print(max(sum))