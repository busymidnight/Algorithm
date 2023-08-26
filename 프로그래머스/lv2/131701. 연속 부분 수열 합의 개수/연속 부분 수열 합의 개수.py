def solution(elements):
    answer = []
    #원형 수열 = 연속된 수열 = 원소를 두 개씩
    cycle = elements * 2
    i = 0
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.append(sum(cycle[i:i+j]))
        
    return len(set(answer))