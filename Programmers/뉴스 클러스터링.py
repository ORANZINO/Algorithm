from collections import defaultdict


def check(s):
    dic = defaultdict(int)
    for i in range(len(s) - 1):
        temp = s[i:i+2]
        if all(ord('a') <= ord(t) <= ord('z') for t in temp):
            dic[temp] += 1
    return dic


def solution(str1, str2):
    dic1 = check(str1.lower())
    dic2 = check(str2.lower())
    u = set(dic1.keys()) | set(dic2.keys())
    if len(u) == 0:
        return 65536
    c = set(dic1.keys()) & set(dic2.keys())
    s1 = sum(max(dic1[i], dic2[i]) for i in u)
    s2 = sum(min(dic1[i], dic2[i]) for i in c)
    return int(s2 / s1 * 65536)


"""
1. lower()를 사용해 모든 글자 소문자로 변환
2. 2글자씩 잘라서 둘 다 알파벳일 경우 dictionary의 key로 만들고 count
3. 두 dictionary의 key들의 교집합과 합집합을 구한다.
4. 합집합이 비었을 경우 그냥 65536을 출력
5. 비어있지 않을 경우 주어진 식에 맞추어 return
"""