def solution(arr):
    answer = [0, 0]

    def dfs(x, y, l):
        if all(arr[i][j] == arr[x][y] for i in range(x, x + l) for j in range(y, y + l)):
            answer[arr[x][y]] += 1
        else:
            l //= 2
            dfs(x, y, l)
            dfs(x + l, y, l)
            dfs(x, y + l, l)
            dfs(x + l, y + l, l)

    dfs(0, 0, len(arr))

    return answer

