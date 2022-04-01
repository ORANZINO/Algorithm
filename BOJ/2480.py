from collections import Counter

counter = Counter(map(int, input().split()))
if len(counter) == 1:
    print(10000 + list(counter.keys())[0] * 1000)
elif len(counter) == 2:
    temp = None
    for key in counter.keys():
        if counter[key] == 2:
            temp = key
            break
    print(1000 + temp * 100)
else:
    print(max(counter.keys()) * 100)

    