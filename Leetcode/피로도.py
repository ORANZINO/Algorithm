def solution(k, dungeons):
    answer = 0
    for i, dungeon in enumerate(dungeons):
        if dungeon[0] <= k:
            answer = max(answer, solution(k - dungeon[1], dungeons[:i] + dungeons[i + 1:]) + 1)
    return answer