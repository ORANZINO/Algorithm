import sys
input = sys.stdin.readline


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


n, m = map(int, input().split())
parent = list(range(n + 1))
edges = []
answer = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
last = 0

for e in edges:
    cost, a, b = e
    two = False
    if find_parent(parent, a) != find_parent(parent, b):
        two = union_parent(parent, a, b)
        answer += cost
        last = cost

print(answer - last)
