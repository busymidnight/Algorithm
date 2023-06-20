from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for k in course:
        array = []
        for menu_li in orders:
            for li in combinations(menu_li, k): # k개의 조합 만들기
                res = ''.join(sorted(li))
                array.append(res)
        sorted_array = Counter(array).most_common() # 조합의 빈도수를 계산 ex) [('ABX',2),('AC',1)]
        answer += [menu for menu, cnt in sorted_array 
                   if cnt > 1 and cnt == sorted_array[0][1]] # 최소 2명 이상이 주문한 메뉴여야 한다
    return sorted(answer)