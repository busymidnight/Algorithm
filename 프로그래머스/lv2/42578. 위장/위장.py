from collections import Counter
from itertools import combinations
def solution(clothes):
    answer = 1
    types = [v for k, v in clothes] #의상 종류만 선택한다
    counts = []
    for type in set(types): #set(types)로 종류 중복 제거함
        counts.append(types.count(type)) #종류별 갯수를 구한다

    for c in counts:
        answer *= c + 1 #종류별로 고르는 방법은 c+1
    
    return answer - 1 #의상을 하나도 고르지 않은 경우를 뺀다
