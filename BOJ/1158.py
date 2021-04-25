n, k = map(int, input().split())
k -= 1
arr = list(range(1, n + 1))
answer = [arr.pop(k)]
temp = k

while arr:
    # k만큼 현재 위치에서 더하기
    temp += k
    # 현재 길이에 맞게 mod 연산하기
    temp %= len(arr)
    # temp 위치에 있는 값 pop하여 정답 리스트에 추가하기
    answer.append(arr.pop(temp))

print(f'<{str(answer)[1:-1]}>')