from math import ceil
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

print(sum(map(lambda x: int(ceil((x - b) / c)) if (x - b) >= 0 else 0, a)) + len(a))

"""
시험장마다 총시험감독관 1명씩 있으므로 시험장의 개수만큼 더한다.
시험장마다 총시험감독관이 맡는 명수만큼 커버가 되지 않는다면 부감독관을 배치한 후 그 수를 합친다.
b만큼 뺐을 때, 0보다 작을 수도 있으므로 이럴 경우를 대비해 조건문을 추가해주었다.
"""