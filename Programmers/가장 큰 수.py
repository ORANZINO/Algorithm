def solution(numbers):
    nums = [str(number) for number in numbers]
    nums.sort(reverse=True, key=lambda x: x * 3)

    return str(int(''.join(nums)))

"""
str으로 바꾸어서 sort하면 백과사전식으로 정렬된다.
그런데 해결해야하는 문제가 있다면 "32"보다 "3"이 더 우선순위가 높다는 점이다.
"32"를 붙이는 것보다 "3"을 붙이는 것이 더 큰 수를 만드는 데 기여하기 때문이다.
이를 위해 numbers의 원소는 모두 1000 이하이므로 3번 반복한 수, 예를 들어 "3"이면 "333"으로 바꾸어 정렬한다.
이렇게 하면 우리가 원하는 우선순위에 맞추어 정렬할 수 있다.
그리고 나서 join한 후 "011" 등을 "11"로 바꾸어주기 위해 int로 바꾸어준 후에 다시 str로 바꾸어 return해준다.
"""