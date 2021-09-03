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