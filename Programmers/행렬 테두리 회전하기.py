def solution(rows, columns, queries):
    matrix = [[i * columns + j for j in range(1, columns + 1)] for i in range(rows)]
    answer = []
    for query in queries:
        x1, y1, x2, y2 = query
        min_val, temp = matrix[x1 - 1][y1 - 1], matrix[x1 - 1][y1 - 1]
        direction = 'r'
        i, j = x1 - 1, y1
        while True:
            matrix[i][j], temp = temp, matrix[i][j]
            min_val = min(min_val, temp)
            if direction == 'r':
                if j == (y2 - 1):
                    direction = 'd'
                    i += 1
                else:
                    j += 1
            elif direction == 'd':
                if i == (x2 - 1):
                    direction = 'l'
                    j -= 1
                else:
                    i += 1
            elif direction == 'l':
                if j == (y1 - 1):
                    direction = 'u'
                    i -= 1
                else:
                    j -= 1
            elif direction == 'u':
                if i == (x1 - 1):
                    break
                else:
                    i -= 1
        answer.append(min_val)
    return answer

