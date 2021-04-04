from collections import deque
from itertools import chain
from copy import deepcopy

routes = []


def dfs(adj, start, store, target):
    if len(list(filter(lambda x: len(x) == target, routes))) > 0:
        pass
    elif not adj[start]:
        routes.append(store)
    else:
        for a in adj[start]:
            temp = deepcopy(adj)
            temp[start].remove(a)

            dfs(temp, a, store + [a], target)


def solution(tickets):
    cities = list(set(list(chain.from_iterable(tickets))))
    cities.sort()
    adj = [[] for _ in cities]
    for t in tickets:
        adj[cities.index(t[0])].append(cities.index(t[1]))
    for i in range(len(adj)):
        adj[i].sort()
    dfs(adj, cities.index("ICN"), [cities.index("ICN")], len(tickets) + 1)
    result = []

    temp = list(filter(lambda x: len(x) == len(tickets) + 1, routes))
    temp.sort()
    for o in temp[0]:
        result.append(cities[o])

    return result
