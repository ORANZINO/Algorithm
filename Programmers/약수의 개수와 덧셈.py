def aliquot_counter(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        temp = aliquot_counter(i)
        if temp % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer


"""
약수 개수를 세는 함수를 만들고 이에 따라 더할건지 뺄건지 결정해서 결과 리턴
"""