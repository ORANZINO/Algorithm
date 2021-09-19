def solution(price, money, count):

    answer = price * count * (count + 1) // 2 - money
    return answer if answer > 0 else 0


"""
1회차이면 1배, 2회차이면 2배를 내는 식이므로 
1~count 까지의 수를 더해서 곱해주면 총 지불해야되는 금액을 구할 수 있다. 
가우스 방법을 사용하여 n(n + 1) / 2 를 해주면 n까지의 합을 구할 수 있다. 
"""