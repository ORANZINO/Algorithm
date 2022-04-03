def solution(numbers):
    def f(x):
        temp = x
        count = 0
        while temp % 2 == 1:
            temp //= 2
            count += 1
        return x + max(1, 2 ** (count - 1))

    return [f(int(num)) for num in numbers]

