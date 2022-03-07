def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    left, right = 0, distance
    answer = None
    while left <= right:
        mid = (left + right) // 2
        now, remove_count, min_interval = 0, 0, distance
        for rock in rocks:
            if (rock - now) < mid:
                remove_count += 1
                if remove_count > n:
                    break
            else:
                min_interval = min(min_interval, rock - now)
                now = rock
        if remove_count > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = min_interval
    return answer

