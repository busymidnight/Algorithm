def solution(prices):
    n = len(prices)
    answer = [0] * n  
    stack = [0] 

    for idx in range(1, n):
        # 가격이 떨어진 경우
        while stack and prices[stack[-1]] > prices[idx]: 
            j = stack.pop() 
            answer[j] = idx - j  # 떨어진 시간
        stack.append(idx)  # 안 떨어진 경우

    while stack: 
        j = stack.pop()
        answer[j] = n - j - 1

    return answer