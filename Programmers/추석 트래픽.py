from datetime import timedelta, datetime


def solution(lines):
    for i, line in enumerate(lines):
        temp = line.split()
        end_time = datetime.strptime(f'{temp[0]} {temp[1]}', '%Y-%m-%d %H:%M:%S.%f')
        lines[i] = (end_time - timedelta(seconds=float(temp[2][:-1]) - 0.001), end_time)
    answer = 1
    for i, line in enumerate(lines):
        count = 1
        temp = line[1] + timedelta(seconds=0.999)
        temp
        for j in range(i + 1, len(lines)):
            if lines[j][0] <= temp:
                count += 1
        answer = max(answer, count)
    return answer


