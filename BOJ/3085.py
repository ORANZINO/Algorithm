import sys
input = sys.stdin.readline


def check(arr):
    answer = 1

    for i in range(n):
        count_r = 1
        count_c = 1
        now_r = arr[i][0]
        now_c = arr[0][i]
        for j in range(1, n):
            if arr[i][j] != now_r:
                answer = max(answer, count_r)
                count_r = 1
                now_r = arr[i][j]
            elif arr[i][j] == now_r:
                count_r += 1
            if arr[j][i] != now_c :
                answer = max(answer, count_c)
                count_c = 1
                now_c = arr[j][i]
            elif arr[j][i] == now_c:
                count_c += 1
            if j == (n - 1):
                answer = max(answer, count_r, count_c)

    return answer


n = int(input())
arr = [list(input().strip()) for _ in range(n)]

ans = 1

for i in range(n):
    for j in range(n):
        if i < (n - 1) and arr[i][j] != arr[i + 1][j]:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            ans = max(ans, check(arr))
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
        if j < (n - 1) and arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            ans = max(ans, check(arr))
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
print(ans)
