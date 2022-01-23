import collections
from typing import *


def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]


"""
주어진 그래프는 방향성이 있는 간선들로 이루어져 있으며, 항상 한붓그리기가 가능하다.
따라서, dfs를 수행하여 한 리스트에 경로를 저장해둠으로써 그 경로를 알아낼 수 있다.
"""