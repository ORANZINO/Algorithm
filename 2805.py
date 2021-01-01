def cut_tree(trees, height):
    temp = list(filter(lambda x: x > height, trees))
    return sum([i-height for i in temp])


n, m = map(int, input().split())
trees = list(map(int, input().split()))

for i in range(max(trees)-1, 1, -1):
    result = cut_tree(trees, i)
    if result >= m:
        break
print(result)

