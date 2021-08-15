def check(x):
    if x < 100:
        return True
    arr = list(map(int, list(str(x))))
    diff = arr[1] - arr[0]
    if all(arr[i + 1] - arr[i] == diff for i in range(1, len(arr) - 1)):
        return True
    else:
        return False


a = int(input())
print(sum(check(i) for i in range(1, a + 1)))

"""
해당 수가 한수인지 아닌지 check하는 함수를 만들었다.
그리고 주어진 범위 내에서 check에서 True가 리턴된 모든 수를 더하면 완성!
"""