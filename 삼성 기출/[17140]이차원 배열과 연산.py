from collections import Counter #개수 세어주는 Counter
r, c, k = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(3)]

def rc_oper():
    max_len = 0
    length = len(data)
    for i in range(length):
        temp = []
        for j in data[i]:
            if j != 0: #0이 아니면 temp에 삽입.
                temp.append(j)
        temp = Counter(temp).most_common() #temp에서 각 원소들에대해 (원소 값, 개수) 형태의 투플을 가진 리스트를 반환함.
        temp.sort(key = lambda x: (x[1], x[0])) #해당 리스트를 sort
        data[i] = [] #데이터 초기화 후 다시 삽입해줌.
        for q, w in temp:
            data[i].append(q)
            if len(data[i]) >= 100: #100개 넘으면 스탑.
                break
            data[i].append(w)
            if len(data[i]) >= 100:
                break
        max_len = max(max_len, len(data[i])) #최대 길이 변경 (0 패딩 해주기 위함)
    for i in range(length): #최대 길이만큼 0 패딩
        for j in range(max_len - len(data[i])):
            data[i].append(0)
        data[i] = data[i][:100]

result = 0
while True:
    try: #중간에 r-1 c-1 만큼 리스트가 존재하지 않을 수도 있음. 예외처리.
        if data[r-1][c-1] == k:
            break
    except:
        pass
    if result >= 100:
        result = -1
        break
    if len(data) < len(data[0]):
        data = list(zip(*data)) #열에서 수행시 zip을 이용한 transpose
        rc_oper()
        data = list(zip(*data))
    else:
        rc_oper()
    result += 1

print(result)