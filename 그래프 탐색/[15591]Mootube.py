#그래프 탐색. dict 이용
import sys

n, quest = map(int, input().split())

videos = dict() #dict 자료형.
for i in range(n-1):
    a, b, r = map(int, input().split())

    #dict에 key : 비디오 번호. value : 다른 비디오, 유사도.
    #삽입.
    if a in videos.keys() :
        videos[a].append([b, r])
    else:
        videos[a] = [[b, r]]

    if b in videos.keys() :
        videos[b].append([a, r])
    else:
        videos[b] = [[a, r]]

for i in range(quest):
    k, v = map(int, input().split())
    visited = [0] * (n+1) #방문. 중복 카운트 방지.
    q = [[v, sys.maxsize]] #q : 확인할 리스트
    while q:
        cn, usado = q.pop() #현재노드와 유사도 pop
        if not visited[cn] and usado >= k: #해당 노드 미방문 & 기준 유사도 넘으면
            visited[cn] = 1 #방문처리
            q.extend(videos[cn]) #해당비디오와 연결된 다른 비디오 큐에 삽입
    count = visited.count(1)
    print(count - 1)
