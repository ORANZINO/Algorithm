# 내 풀이
import sys
input = sys.stdin.readline

def backtrack(k, stack):
    temp = k
    candidates = range(-10, 11)
    for i in range(k + 1):
        now = a[temp]
        if now == '+':
            candidates = [c for c in candidates if (sum(stack[i:k]) + c) > 0]
        elif now == '-':
            candidates = [c for c in candidates if (sum(stack[i:k]) + c) < 0]
        else:
            candidates = [c for c in candidates if (sum(stack[i:k]) + c) == 0]
        temp += (n - (i + 1))
    if k == (n - 1) and candidates:
        global ans
        stack[-1] = candidates[0]
        ans = stack
    else:
        for c in candidates:
            if not ans:
                stack[k] = c
                backtrack(k + 1, stack)


n = int(input())
a = input()
ans = []

backtrack(0, [0 for _ in range(n)])
print(*ans)

# wider93 풀이

n = int(input())
string = input()
b = 0
a = n
x = []
positive = [1, 10, 3, 8, 2, 9, 4, 7, 5, 6]
negative = [-i for i in positive]
zero = [0]

while a:
    x.append(string[b:b + a])
    b += a
    a -= 1
print("x: ", x)
y = {'+':positive, '-':negative, '0': zero}
pool = []
for row in x:
    pool.append(y[row[0]])
print("pool: ", pool)
y = {'+':set(positive), '-':set(negative), '0': {0}}
v = [0]*n
flag = False
def dfs(i, s):
    global flag
    if flag:
        return
    if i == -1:
        flag = True
        print(*v)
        return
    for j in pool[i]:
        v[i] = j
        a = 0
        t = s + j
        for k in range(n - 1, i, -1):
            if t - a not in y[x[i][k-i]]:
                break
            a += v[k]
        else:
            dfs(i-1, t)
dfs(n-1, 0)
