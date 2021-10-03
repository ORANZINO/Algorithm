def solution(sizes):
    for i, size in enumerate(sizes):
        sizes[i] = [max(size), min(size)]

    return max(sizes[i][0] for i in range(len(sizes))) * max(sizes[i][1] for i in range(len(sizes)))

"""
가로세로가 바뀌어서 넣을 경우를 고려할 수 있게 하기 위해서 모든 명함 사이즈 튜플을
(max, min)의 순서로 나열하고 거기서 각 열의 최댓값을 추출해내었다.
"""