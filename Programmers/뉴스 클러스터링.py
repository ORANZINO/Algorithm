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


