def parse_time(time):
    hour, minute = int(time[:2]), int(time[-2:])
    return hour * 60 + minute


def num_to_time(num):
    hour, minute = str(num // 60), str(num % 60)
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return f'{hour}:{minute}'


def solution(n, t, m, timetable):
    start = 540
    dic = {start + i * t: [] for i in range(n)}
    timetable = [parse_time(t) for t in sorted(timetable)]
    for time in timetable:
        for key in dic:
            if time <= key and len(dic[key]) < m:
                dic[key].append(time)
                break
    max_key = max(dic.keys())
    if len(dic[max_key]) < m:
        return num_to_time(max_key)
    else:
        return num_to_time(max(dic[max_key]) - 1)


"""
1. 주어진 시간을 정렬하고 모두 숫자(분)로 환산
2. 가능한 시간을 모두 dictionary의 key로 만든다. -> 버스 나타냄
3. 각 시간의 버스마다 가능한 인원을 모두 태운다.
4. 마지막 시간의 버스가 다 차지 않았을 경우 마지막 버스의 시간을 return
5. 마지막 시간의 버스가 다 찼을 경우 마지막 승객보다 1분 일찍 도착하도록 한다. 
"""