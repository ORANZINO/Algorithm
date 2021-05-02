t = int(input())
c = [int(input()) for _ in range(t)]
max_val = max(c)
# 소수에 대한 정보를 담을 Array
arr = [True] * max_val
arr[0] = False
arr[1] = False
# 소수만 True로 표시하도록 iterate
for i in range(2, max_val):
    if arr[i]:
        j = 2
        while i * j < max_val:
            arr[i * j] = False
            j += 1
# 각 숫자마다 소수끼리 합쳐서 가능한 조합 체크 후 출력
for n in c:
    temp = 0
    for i in range(2, n // 2 + 1):
        if arr[i] and arr[n - i]:
            temp += 1
    print(temp)
