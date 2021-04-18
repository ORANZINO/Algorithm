import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n, m, k = map(int, input().split())
arr = [input() for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())
q = deque()
q.append((x1 - 1, y1 - 1))
distance[x1 - 1][y1 - 1] = 0
steps = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    x, y = q.popleft()
    for step in steps:
        for i in range(1, k + 1):
            next_x, next_y = x + (i * step[0]), y + (i * step[1])
            if next_x == (x2 - 1) and next_y == (y2 - 1):
                print(distance[x][y] + 1)
                exit()
            if 0 <= next_x < n and 0 <= next_y < m and arr[next_x][next_y] == '.':
                if distance[next_x][next_y] == -1:
                    distance[next_x][next_y] = distance[x][y] + 1
                    q.append((next_x, next_y))
                elif (distance[x][y] + 1) > distance[next_x][next_y]:
                    break
            else:
                break
print(-1)

"""
일반적인 BFS 문제이지만 다른 점은 한 번에 많은 칸을 이동하는 것이 가능하다는 것.
4가지 방향으로 모두 갈 수 있을만큼 가는 방식으로 BFS를 수행한다.
이 때 적절히 끊어주는 것이 시간 초과되느냐 마느냐를 좌우한다.
중간에 벽을 만나거나, 맵 밖으로 빠져나가거나, 또는 지금 기록할 수 있는 것보다 적은 거리가 이미 기록돼있을 경우,
탐색을 종료해주도록 한다.
"""