from collections import deque


def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            cache.append(city)
            time += 5
    return time

'''
LRU 알고리즘을 deque를 사용하여 구현, maxlen을 통해 사이즈 제한 가능
'''