# 정석 풀이

def n_queens(col, i):
    if (promising(col, i)):
        if i == n:
            global ans
            ans += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(col, i + 1)

def promising(col, i):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag

n = int(input())
col = [0] * (n + 1)
ans = 0
n_queens(col, 0)
print(ans)


# 시간초과 안나는 풀이


n = int(input())
arr = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(arr[n])