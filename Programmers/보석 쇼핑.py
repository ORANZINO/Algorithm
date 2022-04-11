from collections import defaultdict


def solution(gems):
    counter = defaultdict(int)
    left, gem_count = 0, 0
    gem_list = set(gems)
    answer = [1, len(gems)]

    for right in range(len(gems)):
        counter[gems[right]] += 1
        if counter[gems[right]] == 1:
            gem_count += 1
            if gem_count == len(gem_list):
                while left <= right and counter[gems[left]] > 1:
                    counter[gems[left]] -= 1
                    left += 1
                if right - left < answer[1] - answer[0]:
                    answer = [left + 1, right + 1]
                counter[gems[left]] -= 1
                gem_count -= 1
                left += 1

    return answer

