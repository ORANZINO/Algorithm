import heapq
from collections import deque


def solution(jobs):
    jobs.sort()
    job_index = 1
    ready = [(jobs[0][1], jobs[0][0])]
    now = jobs[0][0]
    total = 0
    while ready or job_index < len(jobs):
        while job_index < len(jobs) and jobs[job_index][0] <= now:
            heapq.heappush(ready, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        if ready:
            work_time, req_time = heapq.heappop(ready)
            now += work_time
            total += now - req_time
        else:
            now = jobs[job_index][0]
    return total // len(jobs)

