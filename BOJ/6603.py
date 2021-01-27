from itertools import combinations

while True:
    array = input().split()
    k = array[0]
    if k == '0':
        break
    array = array[1:]
    for c in combinations(array, 6):
        print(' '.join(c))
    print()
