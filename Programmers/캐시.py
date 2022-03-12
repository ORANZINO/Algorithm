from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = length = 0
    for city in cities:
        city = city.lower()
        try:
            i = cache.index(city)
            cache.remove(city)
            cache.append(city)
            time += 1
        except:
            cache.append(city)
            time += 5
    return time

