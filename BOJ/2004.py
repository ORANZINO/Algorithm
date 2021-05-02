def count_div(target, n):
    count = 0
    temp = target
    while temp != 0:
        temp //= n
        count += temp
    return count

n, m = map(int, input().split())
print(min((count_div(n, 2) - count_div(m, 2) - count_div(n - m, 2)), (count_div(n, 5) - count_div(m, 5) - count_div(n - m, 5))))

"""
처음에는 단순히 곱한 후에 10으로 나누면서 수를 세보려고 했으나,
그런 방식을 취하기에는 주어진 수가 너무 커서 시간 초과가 발생했다.
그래서 주어진 곱셈식에서 2와 5가 총 몇 번씩 들어가있는지 확인 후 더 적은 쪽을 출력해내는 방식을 택하게 되었다.
그리고 팩토리얼 식에서 어떤 수가 약수로 총 몇 번 포함되어있는지 확인하기 위해서는 가장 큰 수를 해당 수로 계속 나누면서
몫을 더해가는 방법이 있다는 것을 알게 되었다.
이런 방식을 취하면 n = 2일 경우 처음에는 2의 배수, 나중에는 4의 배수, 8의 배수의 개수를 구할 수 있다.
"""