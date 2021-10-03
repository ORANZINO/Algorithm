def solution(board, moves):
    n = len(board)
    basket = []
    answer = 0
    for move in moves:
        for i in range(n):
            if board[i][move - 1] > 0:
                if len(basket) > 0 and board[i][move - 1] == basket[-1]:
                    basket.pop(-1)
                    answer += 2
                else:
                    basket.append(board[i][move - 1])
                board[i][move - 1] = 0
                break

    return answer

"""
문제가 요구한 그대로를 구현하면 되는 문제.
각 move마다 해당하는 인형을 뽑아 basket에 넣되, 같은 것이 겹치면 터질 수 있게 한다.
인형을 뽑을 때마다 board의 해당 칸을 빈칸처리해주는 것을 잊지 않도록 한다. 
"""