from collections import Counter

def solution(topping):
    dic = Counter(topping)
    set_dic = set()
    answer = 0
    
    for i in topping:
        dic[i] -= 1 # 토핑을 꺼내서
        set_dic.add(i) # set_dic에 추가
        if dic[i] == 0: # 토핑 갯수가 0이면
            dic.pop(i) # dic에서 삭제
        if len(dic) == len(set_dic): # 토핑 갯수가 같을 때
            answer += 1 
    return answer
