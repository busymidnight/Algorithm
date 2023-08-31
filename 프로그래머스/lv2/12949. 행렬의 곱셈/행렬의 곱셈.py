def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr2)):
                sum += arr1[i][k] * arr2[k][j]
            tmp.append(sum)
        answer.append(tmp)
    
    return answer
