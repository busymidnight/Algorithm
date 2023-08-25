from collections import Counter

def solution(str1, str2):
    #대소문자 상관없으므로 소문자 처리
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    #리스트 선언
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        #알파벳만 리스트에 추가
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
            
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
    #Counter 사용        
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    
    #교집합 원소만 추출
    inter = list((Counter1 & Counter2).elements())
    #합집합 원소만 추출
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        #자카드 유사도 계산
        return int(len(inter) / len(union) * 65536)