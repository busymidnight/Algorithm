from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = 0
    t = Counter(tangerine).most_common(k)
    for i,j in t:
        cnt += j 
        answer += 1 # 
        if cnt >= k: 
            return answer
