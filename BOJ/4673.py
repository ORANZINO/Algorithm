arr = [True] * 10001

for i in range(1, len(arr)):
    if arr[i]:
        temp = i + sum(map(int, list(str(i))))
        while temp <= 10000 and arr[temp]:
            arr[temp] = False
            temp = temp + sum(map(int, list(str(temp))))

for i in range(1, len(arr)):
    if arr[i]:
        print(i)


"""
메모이제이션 방법을 이용해 푼 문제.
10000까지를 나타내는 리스트를 만들고 그 안에서 모든 셀프 넘버들을 만들어 체크했다.
체크되지 않은 수들만 출력하면 완성!
"""