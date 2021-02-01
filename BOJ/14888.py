def tsp(A, op_nums, result):
    ops = ['+', '-', '*', '//']
    if not A:
        global max_result
        global min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    for i in range(4):
        if op_nums[i] > 0:
            op_nums[i] -= 1
            if i == 3 and result < 0:
                tsp(A[1:], op_nums, -(-result // A[0]))
            else:
                tsp(A[1:], op_nums, eval(f'{result}{ops[i]}{A[0]}'))
            op_nums[i] += 1



INF = int(1e9)
n = int(input())
A = list(map(int, input().split()))
op_nums = list(map(int, input().split()))

max_result = -INF
min_result = INF

tsp(A[1:], op_nums, A[0])

print(max_result)
print(min_result)
