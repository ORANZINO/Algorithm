from math import gcd


def solution(arr):
    for i in range(len(arr) - 1):
        if i == 0:
            gcd_val = gcd(arr[i], arr[i + 1])
            lcm_val = arr[i] * arr[i + 1] // gcd_val
        else:
            gcd_val = gcd(lcm_val, arr[i + 1])
            lcm_val = lcm_val * arr[i + 1] // gcd_val

    return lcm_val



"""
Python 내장 함수에 최대공약수를 구하는 것은 있지만 최소공배수를 구하는 것은 없다.
그렇지만 a, b를 곱하고 그것을 최대공약수로 나눠주면 그것이 최소공배수가 된다.
이러한 방식으로 arr에 있는 수에서 순차로 최소공배수를 구해주면 된다.
"""