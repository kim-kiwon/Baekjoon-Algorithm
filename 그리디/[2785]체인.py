#그리디
n = int(input())

arr = list(map(int, input().split()))

arr.sort()
count = 0
while len(arr) > 1:
    a = arr.pop() #제일 긴것
    b = arr.pop() #두번째로 긴것.
    if len(arr) == 0: #원소가 두개 뿐이면 count 증가하고 종료
        count += 1
        break
    arr[0] -= 1 #첫번째 체인 하나를 고리로
    count += 1
    arr.append(a+b) #제일 긴거 두개를 합쳐줌
    if arr[0] == 0: #첫번째 체인 다썻으면 삭제
        del(arr[0])

print(count)