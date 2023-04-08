def solution(brown, yellow):
    total = brown + yellow
    check = []
    h = 0 #가로
    v = 0 #세로
    #최소 3부터이기 때문에 3부터 찾는다
    for i in range(3, total+1):
        if total % i == 0: # total의 약수를 찾는다
            check.append(i)

    for i in range(len(check)): #세로를 기준으로 찾는다
        v = check[i]
        h = int(total/v)
        #세로-2 * 가로-2 == yellow
        if (v-2)*(h-2) == yellow:
            return [h, v]
