from math import ceil
import heapq

def calculate_time(start, end):
    start, end = list(map(int, start.split(':'))), list(map(int, end.split(':')))
    return (end[0] * 60 + end[1]) - (start[0] * 60 + start[1])

def solution(m, musicinfos):
    q = []
    for i, info in enumerate(musicinfos):
        start, end, name, music = info.split(',')
        time = calculate_time(start, end)
        arr = []
        j = 0
        while j < len(music):
            if j != (len(music) - 1) and music[j + 1] == '#':
                arr.append(music[j:j+2])
                j += 2
            else:
                arr.append(music[j])
                j += 1
        music = ''.join((arr * ceil(time / len(arr)))[:time])
        if m[-1] != '#':
            loc1, loc2 = music.find(m), music.find(m + '#')
            while loc1 != -1 and (loc1 == loc2):
                music = music[loc2 + len(m) + 1:]
                loc1, loc2 = music.find(m), music.find(m + '#')
            if loc1 != -1:
                heapq.heappush(q, (-time, i, name))
        elif music.find(m) != -1:
            heapq.heappush(q, (-time, i, name))
    return q[0][2] if q else "(None)"

