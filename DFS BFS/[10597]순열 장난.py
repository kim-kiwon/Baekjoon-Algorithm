#백트래킹 DFS

import sys
n = input()
visit = [0] * 51 #50까지 중복X. 방문확인
arr = []
def solve(idx): #idx : 입력의 몇번째 인덱스를 확인할 것인지
    if idx == len(n): #끝까지 다 확인했다면
        max_num = 0
        for i in range(len(arr)):
            max_num = max(max_num, int(arr[i]))
        if max_num == len(arr): #가장큰 수가 길이와 같다면. ->답
            for i in range(len(arr)):
                print(int(arr[i]), end = ' ')
            sys.exit()
    if idx < len(n) and not visit[int(n[idx])]: #한자리수. 방문X라면.
        visit[int(n[idx])] = 1
        arr.append(n[idx]) #arr에 넣어보고 dfs 진행.
        solve(idx + 1)

        visit[int(n[idx])] = 0 #백트래킹.
        arr.pop()
    if idx + 1 < len(n) and int(n[idx:idx+2]) <= 50 and not visit[int(n[idx:idx+2])]:
        #50이하의 두자리수고 방문안했다면
        visit[int(n[idx:idx+2])] = 1
        arr.append(n[idx:idx+2])
        solve(idx + 2) #위와 동일.

        visit[int(n[idx:idx+2])] = 0
        arr.pop()

solve(0)