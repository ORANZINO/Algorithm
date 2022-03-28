from copy import deepcopy

def solution(n, info):
    answer = [-1]
    now_diff = 0
    def backtrack(index, plan, left, a_score, r_score):
        if index == 10:
            plan[10] = left
            nonlocal now_diff
            if r_score > a_score and now_diff <= (r_score - a_score):
                nonlocal answer
                if now_diff < (r_score - a_score):
                    answer = deepcopy(plan)
                    now_diff = r_score - a_score
                else:
                    answer = deepcopy(max(plan, answer, key=lambda x: list(reversed(x))))
            plan[10] = 0
            return
        temp = info[index] + 1
        if temp <= left:
            plan[index] = temp
            backtrack(index + 1, plan, left - temp, a_score, r_score + (10 - index))
            plan[index] = 0
        if info[index]:
            backtrack(index + 1, plan, left, a_score + (10 - index), r_score)
        else:
            backtrack(index + 1, plan, left, a_score, r_score)
    backtrack(0, [0] * 11, n, 0, 0)
    return answer

