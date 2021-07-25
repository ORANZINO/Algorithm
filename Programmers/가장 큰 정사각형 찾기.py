def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    return max(map(max, board)) ** 2

"""
Dynamic Programming 방식을 이용한 풀이.
2X2 사이즈로 검사하여 오른쪽 끝 위치에 만들 수 있는 정사각형의 사이즈를 표시한다.
주변에 1, 1, 1이 있다면 2X2 정사각형을 만들 수 있고
2, 2, 2가 있다면 3X3 정사각형을 만들 수 있는 원리
"""