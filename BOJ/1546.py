n = int(input())
arr = list(map(int, input().split()))
print(sum(map(lambda x: x / max(arr) * 100, arr)) / n)

'''
각 수를 모두 최댓값으로 나누고 100을 곱해서 평균을 구해준다.
'''