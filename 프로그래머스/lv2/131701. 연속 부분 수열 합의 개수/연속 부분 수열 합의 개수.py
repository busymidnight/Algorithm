def solution(elements):
    answer = []
    #원형 수열 = 연속된 수열 = 원소를 두 개씩
    cycle = elements * 2
    i = 0
    elem_sum = 0
    for i in range(len(elements)):
        for j in range(len(elements)):
            elem_sum = sum(cycle[i:i+j])
            answer.append(elem_sum)
        
    return len(set(answer))