from math import gcd


def solution(w,h):
    return w * h - (w + h - (gcd(w, h)))

"""
w + h를 더한 것에서 w와 h의 최대공약수를 뺀 것만큼 대각선상의 사각형이 생성된다는 것을 알 수 있다.
"""