
def solution(s):
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key in dic:
        s = s.replace(key, dic[key])
    return int(s)

"""
모든 문자열을 dictionary에서 찾아서 숫자로 replace해준다.
"""