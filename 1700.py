from copy import deepcopy

n, k = map(int, input().split())
arr = list(map(int, input().split()))
now = []
answer = 0
temp = -1
for idx, item in enumerate(arr):
    if item not in now:
        if len(now) < n:
            now.append(item)
        else:
            after = arr[idx+1:]
            dup_now = deepcopy(now)
            for i, x in enumerate(now):
                try:
                    if after.index(x) > temp:
                        temp = after.index(x)
                    if i == (len(now) - 1):
                        dup_now.remove(after[temp])
                        dup_now.append(item)
                        answer += 1
                except:
                    if x not in after:
                        dup_now.remove(x)
                        dup_now.append(item)
                        answer += 1
                        break
            temp = -1
            now = deepcopy(dup_now)
print(answer)