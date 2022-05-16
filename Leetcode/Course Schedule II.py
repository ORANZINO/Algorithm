class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, answer = [[] for _ in range(numCourses)], []
        indegree, q = [0] * numCourses, collections.deque()

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            temp = q.popleft()
            for g in graph[temp]:
                indegree[g] -= 1
                if indegree[g] == 0:
                    q.append(g)
            answer.append(temp)

        return answer if len(answer) == numCourses else []

    