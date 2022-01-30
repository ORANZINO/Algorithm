import collections
from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        trace, visited = set(), set()

        def dfs(i):
            if i in trace:
                return False
            if i in visited:
                return True
            trace.add(i)
            for g in graph[i]:
                if not dfs(g):
                    return False
            trace.remove(i)
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

"""
Cycle이 만들어지는지 여부를 검사하는 문제이다.
DFS를 통해서 node들을 방문하되 새로 방문하게 되는 노드를 이미 방문한 적이 있다면 False를, 그 외의 경우에는 True를 
리턴한다.
"""