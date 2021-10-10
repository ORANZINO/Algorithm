def solution(number, k):
    number = list(number)
    alive = [True for _ in range(len(number))]
    i = 0
    while k:
        if i == len(number) - 1:
            j = -1
            while k:
                alive[j] = False
                k -= 1
        elif number[i] < number[i + 1]:
            alive[i] = False
            k -= 1
            j = i - 1
            while k and j >= 0:
                if alive[j]:
                    if number[j] < number[i + 1]:
                        alive[j] = False
                        k -= 1
                    else:
                        break
                j -= 1
        i += 1
    return ''.join(number[i] for i in range(len(number)) if alive[i])


"""
시간 줄이는 것이 까다로웠던 문제.
list로 만들고 중간에 pop하는 방식을 취했으나 시간복잡도의 문제도 인덱싱해서 마킹하는 방식을 취했다.
다 같은 숫자일 때의 처리를 해주는 것을 잊으면 안된다.
"""