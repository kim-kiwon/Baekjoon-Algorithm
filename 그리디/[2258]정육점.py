#그리디. sys.maxsize = 최대값.

import sys
n, m = map(int, input().split())

#가격 같은 고기는 무료로 안주는 것에 유의.

meat = []
for _ in range(n):
    gram, price = map(int, input().split())
    meat.append([price, gram])

#가격 오름차순. 무게 내림차순 정렬.
meat.sort(key = lambda x: (x[0], -x[1]))

ans = sys.maxsize
weight, same =  0, 0
flag = False

for i in range(n):
    weight += meat[i][1] #누적합
    if i >= 1 and meat[i][0] == meat[i-1][0]:
        #전것과 가격이 같으면
        same += meat[i][0]
        #same에 같은 무게 비용 저장.
    else:
        same = 0
    if weight >= m:
        ans = min(ans, meat[i][0] + same) #가격이 동일한 고기 있으면 해당 값 더하기.
        flag = True

print(ans if flag else -1)