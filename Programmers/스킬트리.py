def solution(skill, skill_trees):
    skill_dic = {skill[i]: i for i in range(len(skill))}
    answer = 0
    for tree in skill_trees:
        count = 0
        for i, c in enumerate(tree):
            if c in skill:
                if count == skill_dic[c]:
                    count += 1
                else:
                    break
            if i == len(tree) - 1:
                answer += 1
    return answer


"""
각 문자마다 스킬트리 순서대로 되어있는지 hash table을 사용하여 점검하였다.
"""