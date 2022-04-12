def time_to_sec(time):
    hour, minute, second = map(int, time.split(':'))
    return hour * 3600 + minute * 60 + second


def sec_to_time(sec):
    return ':'.join([str(sec // 3600).zfill(2), str(sec % 3600 // 60).zfill(2), str(sec % 60).zfill(2)])


def solution(play_time, adv_time, logs):
    play_time, adv_time = time_to_sec(play_time), time_to_sec(adv_time)
    total_time = [0] * (play_time + 1)
    for log in logs:
        start, end = map(time_to_sec, log.split('-'))
        total_time[start] += 1
        total_time[end] -= 1
    for _ in range(2):
        for i in range(1, play_time + 1):
            total_time[i] += total_time[i - 1]
    answer, max_time = 0, total_time[adv_time - 1]
    for i in range(adv_time, play_time):
        if total_time[i] - total_time[i - adv_time] > max_time:
            max_time = total_time[i] - total_time[i - adv_time]
            answer = i - adv_time + 1
    return sec_to_time(answer)

