def solution(n, times):
    left = 1
    right = max(times) * n
    mid = (left + right) // 2
    answer = 0
    while left <= right:
        count = 0
        for time in times:
            count += mid // time
            if count >= n:
                break
        if count >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
        mid = (left + right) // 2
    return answer


"""
이분 탐색을 사용하여 심사시간의 최솟값을 탐색하면 된다.
left는 최소 탐색시간인 1, right는 times 중 최댓값을 n번 반복한 수로 한다.
그리고 이분탐색하며 n명을 심사할 수 있는 시간인 경우, answer를 update한다.
"""