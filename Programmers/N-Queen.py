def solution(n):
    def n_queens(row):
        if row == n:
            nonlocal answer
            answer += 1
            return
        for i in range(n):
            nonlocal cols
            cols[row] = i
            flag = True
            for j in range(row):
                if abs(cols[row] - cols[j]) == row - j or cols[row] == cols[j]:
                    flag = False
                    break
            if flag:
                n_queens(row + 1)

    cols = [0] * n
    answer = 0
    n_queens(0)
    return answer


