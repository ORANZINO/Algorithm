def process(s):
    if len(s) > 1:
        return s[0].upper() + s[1:].lower()
    elif len(s) == 1:
        return s[0].upper()
    else:
        return ''


def solution(s):
    return ' '.join(process(a) for a in s.split(' '))


"""
split으로 처리해주면 간단한데 space가 2개 이상 이어지는 경우를 고려해야 한다.
split(' ')로 해주면 두 space 사이의 길이가 0인 문자열을 발견할 수 있는데, 이런 경우
그대로 놔두고 join하는 방식을 취하면 된다.
"""