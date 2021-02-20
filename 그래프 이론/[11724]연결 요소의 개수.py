n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    u, v = map(int, input().split())
    union_parent(parent, u, v)

for i in range(1, n+1):
    find_parent(parent, i)

parent_set = set()

for i in range(1, n+1):
    parent_set.add(parent[i])

print(len(parent_set))