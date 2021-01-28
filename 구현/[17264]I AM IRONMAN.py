N, P = list(map(int, input().split()))
W, L, G = list(map(int, input().split()))

win =[]
lose = []

for i in range(P):
    name, game = input().split()
    if game == 'W':
        win.append(name)
    else:
        lose.append(name)

score = 0
up = 0

for i in range(N):
    player = input()
    if player in win:
        score += W
    else:
        score -= L
        if score < 0:
            score = 0
    if score >= G:
        print("I AM NOT IRONMAN!!")
        up = 1
        break

if up == 0:
    print("I AM IRONMAN!!")