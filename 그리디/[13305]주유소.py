#그리디. 최소의 기름요금을 선택해나감.

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

now = price[0] #now : 지금까지 최소 기름 요금.
result = 0
for i in range(len(dist)):
    now = min(now, price[i]) #도시 도착시마다 최소 기름 요금 갱신.
    result += now * dist[i] #최소 기름요금으로 다음 도시까지
print(result)