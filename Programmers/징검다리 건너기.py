# Solution 1 (효율성 통과 X)

from collections import Counter

def solution(stones, k):
    temp = stones[:k]
    max_val = answer = max(temp)
    counter = Counter(temp)
    left = 0
    if stones[0] == 200000000:
        return stones[-1]
    for right in range(k, len(stones)):
        counter[stones[right]] += 1
        if counter[stones[right]] == 1 and stones[right] > max_val:
            max_val = stones[right]
        if counter[stones[left]] == 1:
            del counter[stones[left]]
            if stones[left] == max_val:
                max_val = max(counter.keys())
                answer = min(max_val, answer)
        else:
            counter[stones[left]] -= 1
        left += 1
    return answer

# Solution 2


def solution(stones, k):
    left, right = 1, 200000000
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt == k:
                    break
            elif cnt > 0:
                cnt = 0
        if cnt == k:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    return answer

