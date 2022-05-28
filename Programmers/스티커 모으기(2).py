def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker)
    arr1, arr2 = [0] * (n - 1), [0] * (n - 1)
    arr1[0], arr1[1] = sticker[0], max(sticker[0], sticker[1])
    arr2[0], arr2[1] = sticker[1], max(sticker[1], sticker[2])

    for i in range(2, n - 1):
        arr1[i] = max(sticker[i] + arr1[i - 2], arr1[i - 1])
        arr2[i] = max(sticker[i + 1] + arr2[i - 2], arr2[i - 1])

    return max(arr2[-1], arr1[-1])