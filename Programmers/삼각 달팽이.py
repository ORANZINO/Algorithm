def solution(n):
    steps = [(1, 0), (0, 1), (-1, -1)]
    step_idx = 0
    answer = [[0] * i for i in range(1, n + 1)]
    i = 1
    x = y = 0
    while i <= (n * (n + 1) // 2):
        answer[x][y] = i
        i += 1
        nx, ny = x + steps[step_idx][0], y + steps[step_idx][1]
        if 0 <= nx < n and 0 <= ny < len(answer[nx]) and answer[nx][ny] == 0:
            x, y = nx, ny
        else:
            step_idx = (step_idx + 1) % 3
            x, y = x + steps[step_idx][0], y + steps[step_idx][1]
    return sum(answer, [])

