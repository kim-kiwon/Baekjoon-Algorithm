N = int(input())
#0으로 영향 줄수 있는 놈들의합. 영향 줄수 없는 놈들의 합 구분. -> 각각 배열이 지들끼리 같아야함.

arr = [] #처음배열
checksum = [] #0존재하는 행,열 저장배열
for i in range(N):
    arr2 = list(map(int , input().split()))
    for j in range(N):
        if arr2[j] == 0:
            a = i
            b = j
    arr.append(arr2)
#처음배열 만들고. 0존재하는 열과행 a,b 에저장

axissum = [] #0존재하지 않는 열,행,대각선의합 저장할배열
for i in range(N):
    if i != a:
        axissum.append(sum(arr[i]))
    else:
        checksum.append(sum(arr[i]))
    #가로합 삽입

arr2 = list(zip(*arr))

for i in range(N):
    if i != b:
        axissum.append(sum(arr2[i]))
    else:
        checksum.append(sum(arr2[i]))
    #세로합 삽입

cross = 0
cross2 = 0
for i in range(N):
    cross += arr[i][i]
    cross2 += arr[i][N-1-i]

if a!=b : axissum.append(cross)
else : checksum.append(cross)

if b!= (N-1-a) : axissum.append(cross2)
else : checksum.append(cross2)
#대각선 합들 삽입

flag = 1
if len(set(axissum)) != 1: flag = 0
if len(set(checksum)) != 1: flag = 0
#set: unique 한것만 추려줌. len(set(배열))이 1이다 => 자기들끼리 모두 같다.

if flag == 1:
    print(axissum[0] - checksum[0])
else:
    print(-1)

