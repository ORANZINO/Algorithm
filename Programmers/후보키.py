from itertools import combinations

def solution(relation):
    row, col = len(relation), len(relation[0])
    candidates = []
    answer = []
    for i in range(1, col + 1):
        candidates.extend(combinations(list(range(col)), i))
    for c in candidates:
        temp = [tuple(student[i] for i in c) for student in relation]
        if len(set(temp)) == row:
            flag = False
            for keys in answer:
                if set(keys).issubset(set(c)):
                    flag = True
                    break
            if not flag: answer.append(c)
    return len(answer)

