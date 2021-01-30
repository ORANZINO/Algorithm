def cut(x):
    global trees
    return sum(t - x if t > x else 0 for t in trees)


n, m = map(int, input().split())
trees = list(map(int, input().split()))
high_limit = max(trees)
low_limit = high_limit - m
mid = (high_limit + low_limit) // 2
cut_tree = cut(mid)
answer = mid

while low_limit <= high_limit:
    if cut_tree > m:
        answer = mid
        low_limit = mid + 1
    elif cut_tree < m:
        high_limit = mid - 1
    else:
        answer = mid
        break
    mid = (high_limit + low_limit) // 2
    cut_tree = cut(mid)

print(answer)


