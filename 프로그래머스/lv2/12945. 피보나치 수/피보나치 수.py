def solution(n):
    d = [0] *100001
    d[1], d[2] = 1, 1
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]   
    return d[n] % 1234567