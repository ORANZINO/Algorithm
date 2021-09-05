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


"""
모든 line에 대해서 시작시간과 끝 시간을 표시
모든 line에 대해 이후의 line들이 1초 내에 포함되는지 검사
제일 많은 line이 포함된 경우를 return
"""