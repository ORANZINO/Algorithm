def solution(name):
    dist = [min(ord(n) - ord('A'), 26 - (ord(n) - ord('A'))) for n in name]
    i = 0
    answer = 0

    while True:
        answer += dist[i]
        dist[i] = 0
        if all(d == 0 for d in dist):
            break
        left = 1
        right = 1
        while dist[i - left] == 0 and left < len(dist):
            left += 1
        while dist[i + right] == 0 and right < len(dist):
            right += 1
        if right <= left:
            i += right
            answer += right
        else:
            i -= left
            answer += left

    return answer

"""
각 알파벳마다 최소 움직임을 계산해놓는다.
첫 번째 자리에서 출발해 가장 가까운 조이스틱 위아래 움직임이 필요한 곳을 찾아 좌우 움직임을 한다.
다 변경되었으면 종료 후 조이스틱 움직임 개수 카운트
"""