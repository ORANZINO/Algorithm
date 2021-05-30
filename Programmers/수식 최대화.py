from itertools import permutations


def solution(expression):
    answers = []
    tokens = []
    ops = set()
    point = 0

    for i in range(len(expression)):
        if expression[i] in ['+', '-', '*']:
            tokens.append(expression[point:i])
            tokens.append(expression[i])
            ops.add(expression[i])
            point = i + 1
        elif i == len(expression) - 1:
            tokens.append(expression[point:])

    for order in permutations(ops, len(ops)):
        temp_tokens = tokens[:]
        for op in order:
            while op in temp_tokens:
                op_idx = temp_tokens.index(op)
                temp = eval(''.join(temp_tokens[op_idx - 1:op_idx + 2]))
                del temp_tokens[op_idx - 1:op_idx + 2]
                temp_tokens.insert(op_idx - 1, str(temp))
        answers.append(abs(int(temp_tokens[0])))
    print(answers)
    return max(answers)

"""
string으로 입력된 expression을 전처리하고 나서
존재하는 operator들의 우선순위를 모두 시도해본다.
그렇게 해서 가장 큰 수를 산출하는 경우를 리턴한다.
논리는 간단하지만 구현이 조금 귀찮은 문제.
"""