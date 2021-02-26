#처음부터 채워나가는 그리디
n, l = map(int, input().split())

pool = [] #웅덩이 위치 저장
for _ in range(n):
    s, e = map(int, input().split())
    pool.append((s, e))

pool.sort(key = lambda x : (-x[0], -x[1])) #pop활용 위해 역순 정렬

count = 0 #널빤지 수
now = pool[-1][0] #현재 널빤지 놓기 시작하는 칸

while pool:
    s, e = pool.pop()
    now = max(now, s) #현재 확인중인칸 = 전칸 널빤지 이어서 vs 이번 웅덩이 시작칸 중 더 큰값.
    while True:
        if now >= e: #널빤지 시작이 웅덩이 끝 넘어서면 break
            break
        now += l #널빤지 길이만큼 이동
        count += 1

print(count)

