def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    parent, answer = list(range(n)), 0

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(a, b):
        a, b = find_parent(a), find_parent(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    for x, y, cost in costs:
        if find_parent(x) != find_parent(y):
            union_parent(x, y)
            answer += cost
    return answer

