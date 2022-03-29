from math import ceil
from collections import defaultdict


def convert(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute


def solution(fees, records):
    def time_to_money(time):
        time -= fees[0]
        result = fees[1]
        if time <= 0:
            return result
        result += ceil(time / fees[2]) * fees[3]
        return result

    log, answer = dict(), defaultdict(int)
    for record in records:
        time, car_id, op = record.split()
        time = convert(time)
        if op == "IN":
            log[car_id] = time
        else:
            answer[car_id] += time - log[car_id]
            del log[car_id]
    for car_id in log:
        answer[car_id] += 1439 - log[car_id]
    for car_id in answer:
        answer[car_id] = time_to_money(answer[car_id])
    return [item[1] for item in sorted(answer.items())]

