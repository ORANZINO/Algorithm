def min_backtrack(now, marks):
    for i in range(10):
        temp = now + [str(i)]
        if eval(''.join(temp)) and str(i) not in now:
            global min_ans
            if not marks and not min_ans:
                min_ans = ''.join(t for t in temp if t not in ['<', '>'])
            elif not min_ans:
                min_backtrack(temp + [marks[0]], marks[1:])

def max_backtrack(now, marks):
    for i in range(9, -1, -1):
        temp = now + [str(i)]
        if eval(''.join(temp)) and str(i) not in now:
            global max_ans
            if not marks and not max_ans:
                max_ans = ''.join(t for t in temp if t not in ['<', '>'])
            elif not max_ans:
                max_backtrack(temp + [marks[0]], marks[1:])

k = int(input())
mark = input().split()
min_ans = 0
max_ans = 0
for i in range(10):
    min_backtrack([str(i), mark[0]], mark[1:])
    if min_ans: break
for i in range(9, -1, -1):
    max_backtrack([str(i), mark[0]], mark[1:])
    if max_ans: break
print(max_ans)
print(min_ans)
