class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h, w = len(grid), len(grid[0])
        visited = [[False] * w for _ in range(h)]
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and not visited[i][j]:
                    q = collections.deque()
                    q.append((i, j,))
                    visited[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for step in steps:
                            nx, ny = x + step[0], y + step[1]
                            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == '1':
                                q.append((nx, ny,))
                                visited[nx][ny] = True
                    count += 1
        return count
