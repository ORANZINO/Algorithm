
def upgrade(s):
    dic = {"A": "E", "E": "I", "I": "O", "O": "U"}
    if s[-1] != "U":
        return s[:-1] + dic[s[-1]]
    else:
        return upgrade(s[:-1])


def solution(word):
    temp = "A"
    answer = 1
    while temp != word:
        if len(temp) < 5:
            temp += "A"
        else:
            temp = upgrade(temp)
        answer += 1

    return answer


"""
주어진 규칙에 따라 사전 순서대로 단어들을 하나씩 나열하여 몇 번째인지 파악하였다.
AEEEE 와 같은 단어를 업그레이드하는 데에 recursion 활용
"""