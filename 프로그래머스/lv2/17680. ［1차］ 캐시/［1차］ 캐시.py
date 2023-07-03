from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            cache.appendleft(city)
        else:
            cache.remove(city)
            cache.appendleft(city)
            answer += 1
    
    return answer