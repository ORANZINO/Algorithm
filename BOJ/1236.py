n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]
rows = list(range(n))
cols = list(range(m))
for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            if i in rows:
                rows.remove(i)
            if j in cols:
                cols.remove(j)

print(max(len(rows), len(cols)))

"""
모든 row와 col에 경비원이 존재해야 하므로, 이미 존재한다면 해당 row와 col은 제거한다.
남은 row와 col의 개수 중에서 더 큰 값을 프린트한다.
"""