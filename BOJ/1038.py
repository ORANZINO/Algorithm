arr = []
def solution(n):
    num = 0
    for _ in range(n):
        arr.append(num)
        if num == 9876543210:
            break
        if num < 9:
            num += 1
            continue
        str_num = list(str(num))
        flag = False
        for i in range(len(str_num) - 1, -1, -1):
            if int(str_num[i - 1]) - int(str_num[i]) > 1:
                str_num[i] = str(int(str_num[i]) + 1)
                str_num = str_num[:i + 1] + list(map(str, range(len(str_num) - i - 2, -1, -1)))
                num = int(''.join(str_num))
                flag = True
                break
        if not flag:
            if str_num[0] != '9':
                str_num = list(str(int(str_num[0]) + 1)) + list(map(str, range(len(str_num) - 2, -1, -1)))
            else:
                str_num = list(map(str, range(len(str_num) - 1, -1, -1)))
                str_num.insert(0, str(int(str_num[0]) + 1))
            num = int(''.join(str_num))
    return num




n = int(input())
print(-1 if n > 1022 else solution(n))
