'''
t = 테스트 수.
n = 성냥개비 수.
성냥개비를 사용해 만들 수 있는 가장 큰 수와 작은 수 출력.
0으로 시작불가.
data[i] 는 i 만드는데 필요한 성냥개비 개수.
'''
'''
풀이 방식.
dfs 돌면서 성냥개비 개수 0보다 작아질때 까지 -> 탈출문.
성냥개비 개수와 지금까지 만든 문자열이 넘겨주는 인자가됨.

'''
import sys
indx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

t = int(input())
dp = [0 for _ in range(101)] #작은놈 저장
#큰놈은 그냥 1넣고 못넣으면 맨앞에 7.

def dfs(now, rest):
    global min_val, n
    if rest < 0:
        return
    if rest == 0:
        min_val = min(int(now), min_val)
        if dp[n] == 0:
            dp[n] = str(min_val)
        return
    for i in range(10):
        if rest == n and i == 0 : continue
        dfs(now + str(i), rest - data[i])

for _ in range(t):
    min_val = sys.maxsize
    n = int(input())

    #max_val 구하는 규칙 존재.
    a, b = divmod(n, 2)
    max_val = "1" * a if b == 0 else "7" + ("1" * (a-1))

    #min_val만 구하면된다.
    if dp[n] != 0: #이미 값 저장된 놈들.
        print(dp[n], max_val)
    elif n < 14: #규칙 안통하는 놈들.
        dfs("", n)
        print(min_val, max_val)
    else: #규칙 있는 놈들.
        a, b = divmod(n, 7)
        if b == 0:
            dp[n] = str(8) * a
        elif b == 1:
            dp[n] = str(10) + str(8) * (a-1)
        elif b == 2:
            dp[n] = str(1) + str(8) * a
        elif b == 3:
            dp[n] = str(200) + str(8) * (a - 2)
        elif b == 4:
            dp[n] = str(20) + str(8) * (a-1)
        elif b == 5:
            dp[n] = str(2) + str(8) * a
        elif b == 6:
            dp[n] = str(6) + str(8) * a
        print(dp[n], max_val)