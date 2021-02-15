#문자열 이분탐색

n, m = map(int, input().split())

data =[] #포켓몬 도감
for i in range(n):
    data.append((i + 1, input()))

sorted_data = sorted(data, key = lambda x : x[1]) #sorted_data = 이름기준 정렬한 것

def binary_search(target): #이름 기준 정렬한 것에서. target의 이름을 갖는 포켓몬의 투플을 찾는 이분탐색.
    start = 0
    end = len(sorted_data) - 1
    while 1:
        mid = (start + end) // 2
        if sorted_data[mid][1] == target:
            return sorted_data[mid][0]
        elif sorted_data[mid][1] > target:
            end = mid - 1
        else:
            start = mid + 1

quest = []
for _ in range(m):
    quest.append(input())

for i in quest:
    if i.isdigit(): #숫자로만 구성시
        print(data[int(i)-1][1]) #숫자-1번째 이름 출력
    else: #문자로만 구성시
        print(binary_search(i)) #이분탐색으로 해당 이름 갖는 포켓몬 번호출력