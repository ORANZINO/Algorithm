from math import sqrt

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)


def my_solution(n):
    array = [True] * (n + 1)
    array[0] = False
    array[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

    answer = array.count(True)
    return answer