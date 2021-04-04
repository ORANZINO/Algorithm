def solution(begin, target, words):
    answer = 0

    words = [begin] + words
    if target in words:
        target = words.index(target)
    else:
        return 0
    visited = [False] * len(words)
    adj = [[0]*len(words) for _ in range(len(words))]
    for i in range(len(words)):
        for j in range(len(words)):
            count = 0
            for k in range(len(begin)):
                if list(words[i])[k] != list(words[j])[k]:
                    count += 1
            if count == 1:
                adj[i][j] = 1
    q = [0]

    while True:
        daum = []
        for i in q:
            visited[i] = True
            for j in range(len(words)):
                if adj[i][j] and (not visited[j]) and (j not in q):
                    daum.append(j)
        if len(daum) == 0:
            answer = 0
            break
        else:
            q = daum
            answer += 1
            if target in q:
                break

    return answer
