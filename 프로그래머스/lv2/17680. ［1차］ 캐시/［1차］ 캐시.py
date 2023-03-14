def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache: #cache hit:캐시 안에 해당 city가 있음
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: #cache miss: 캐시 안에 해당 city 없음
            if len(cache) < cacheSize: #캐시에 자리가 있음
                cache.append(city)
            elif len(cache) == cacheSize: #캐시가 가득 참
                cache.append(city)
                cache.pop(0) #첫번째 pop
            answer += 5
    return answer