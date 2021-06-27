import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = [100001 for i in range(k + 1)]
ans[0] = 0

for i in arr:
    for j in range(i, k + 1):
        ans[j] = min(ans[j], ans[j - i] + 1)

print(-1 if ans[k] == 100001 else ans[k])

# 입력된 수마다 정해진 범위 내에서 커버할 수 있는 수들을 체크하고 체크되지 못했을 경우 커버할 수 없다고 출력
