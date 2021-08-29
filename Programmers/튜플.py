def solution(s):
    s = '[' + s[1:-1] + ']'
    s = eval(s)
    s.sort(key=lambda x: len(x))
    for i in range(len(s) - 1, 0, -1):
        s[i] = s[i] - s[i - 1]
    return [list(i)[0] for i in s]


"""
주어진 문자열을 집합을 담은 배열로 변환한다.
집합의 길이에 따라 정렬해준다.
끝에서부터 차집합을 구해줌으로써 원래의 순서를 찾는다.
이중 배열을 풀어서 리턴해준다.
"""