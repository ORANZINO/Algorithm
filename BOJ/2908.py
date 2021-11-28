arr = list(map(list, input().split()))
arr[0].reverse()
arr[1].reverse()
arr.sort()
print(''.join(arr[1]))


"""
입력받은 수를 뒤집은 후에 더 큰 수를 출력한다
"""