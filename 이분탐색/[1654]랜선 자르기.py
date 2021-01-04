from sys import stdin

K, N = map(int, stdin.readline().split())
arr = [int(stdin.readline()) for _ in range(K)]

start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in arr:
        count += i // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
