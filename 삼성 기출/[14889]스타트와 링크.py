from itertools import combinations

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

players = [i for i in range(n)]

choice = list(combinations(players, n//2))

result = 1e9
for c in choice:
    a_val = 0
    b_val = 0
    team_a = c
    team_b = []
    for i in range(n):
        if i not in team_a:
            team_b.append(i)
    for a in team_a:
        for p in players:
            if p in team_a:
                a_val += data[a][p]
    for b in team_b:
        for p in players:
            if p in team_b:
                b_val += data[b][p]
    result = min(result, abs(a_val - b_val))

print(result)