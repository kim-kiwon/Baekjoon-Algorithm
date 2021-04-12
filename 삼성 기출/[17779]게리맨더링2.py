'''
1. 5번 선거구를 도출해내는 것이 핵심. 나머지는 주어진 조건 통해 쉽게 도출 가능.
2. 최대 데이터크기 20x20으로 중첩 for문 사용 가능
'''

n = int(input())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

def check(nx, ny):
    if 0<= nx < n and 0 <= ny < n: return True
    else: return False

result = 1e9
for x in range(n):
    for y in range(n): #모든 위치에서
        for d1 in range(n):
            for d2 in range(n): #모든 가능한 d1 d2 값에 대해
                if x < x+ d1 + d2 < n and 0 <= y - d1 < y < y + d2 < n: #주어진 조건에 맞다면
                    val = [0, 0, 0, 0, data[x][y]] #각 선거구별 인구
                    five_val = [] #5번 선거구에 해당하는 칸들

                    #x, y, d1, d2 이용 5번선거구 찾아내기
                    flag = 0 #5번 선거구 경계가 데이터 밖으로 벗어나는지 여부
                    temp = [(x, y)] #5번 선거구 경계를 저장할 리스트
                    nx, ny = x, y
                    for a in range(d1): #좌상단
                        nx += 1
                        ny -= 1
                        if not check: flag = 1; break;
                        val[4] += data[nx][ny]
                        temp.append((nx, ny))
                    if flag == 1: continue
                    for a in range(d2): #좌하단
                        nx += 1
                        ny += 1
                        if not check: flag = 1; break;
                        val[4] += data[nx][ny]
                        temp.append((nx, ny))
                    if flag == 1: continue

                    nx, ny = x, y
                    for a in range(d2): #우상단
                        nx += 1
                        ny += 1
                        if not check: flag = 1; break;
                        val[4] += data[nx][ny]
                        temp.append((nx, ny))
                    if flag == 1: continue
                    for a in range(d1): #우하단
                        nx += 1
                        ny -= 1
                        if not check: flag = 1; break;
                        if a == d1-1: #5번 선거구 아래 꼭지점. 좌하단에서 이미 삽입함. 따로 조건 빼줌
                            if (nx, ny) not in temp: flag = 1; break;
                            break
                        val[4] += data[nx][ny]
                        temp.append((nx, ny))
                    if flag == 1: continue

                    temp.sort(key = lambda x: (x[0], x[1])) #(행, 열) 기준 정렬. 같은 행끼리 그 사이값들 5번선거구로 넣어주려고
                    five_val.extend(temp) #일단 경계 저장.
                    temp = temp[1:-1] #처음끝 빼줌
                    for a in range(0, len(temp), 2): #같은 행의 두점 사이의 값들 모두 5번 선거구로.
                        rnum = temp[a][0]
                        sindex = temp[a][1]
                        dindex = temp[a+1][1]
                        for b in range(sindex + 1, dindex):
                            five_val.append((rnum, b))
                            val[4] += data[rnum][b]

                    #나머지 선거구들 찾기
                    for r in range(n):
                        for c in range(n):
                            if (r, c) in five_val: continue
                            elif 0 <= r < x + d1 and 0 <= c <= y:
                                val[0] += data[r][c]
                            elif 0 <= r <= x + d2 and y < c < n:
                                val[1] += data[r][c]
                            elif x + d1 <= r < n and 0 <= c < y - d1 + d2:
                                val[2] += data[r][c]
                            elif x + d2 < r < n and y - d1 + d2 <= c < n:
                                val[3] += data[r][c]

                    #결과 도출
                    result = min(result, max(val) - min(val))

print(result)