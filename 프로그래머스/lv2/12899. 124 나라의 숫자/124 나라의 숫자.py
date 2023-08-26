def solution(n):
    answer = ''
    while n != 0:
        if n % 3: #3의 배수가 아님 
            answer += str(n%3)
            n //= 3
        else:
            answer += '4'
            n = n // 3 - 1
    return answer[::-1]