def solution(n, edge):
    graph = [[] for _ in range (n + 1)]
    distance = [-1 for _ in range(n + 1)]
    for v in edge:
        a, b = v
        graph[a].append(b)
        graph[b].append(a)
    now = [1]
    next = []
    distance[1] = 0
    d = 0
    while now:
        for n in now:
            for i in graph[n]:
                if distance[i] == -1:
                    next.append(i)
                    distance[i] = d + 1
        now = next.copy()
        next = []
        d += 1
    return distance.count(max(distance))

"""
BFS를 통해서 1번과 각 노드들의 거리를 구한다.
최대 거리인 노드들이 몇개인지 카운트하여 리턴한다.
"""