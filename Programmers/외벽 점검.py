from itertools import permutations


def solution(n, weak, dist):
    length, answer = len(weak), len(dist) + 1
    for i in range(length):
        weak.append(weak[i] + n)

    for start in range(length):
        for friends in permutations(dist, len(dist)):
            count = 1
            end = weak[start] + friends[count - 1]
            for index in range(start + 1, start + length):
                if weak[index] > end:
                    count += 1
                    if count > len(dist):
                        break
                    end = weak[index] + friends[count - 1]
            answer = min(answer, count)

    return answer if answer <= len(dist) else -1

