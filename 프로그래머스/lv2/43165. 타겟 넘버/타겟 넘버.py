def solution(numbers, target):

    def dfs(n, sum, numbers,target):
        nonlocal answer
        if n == len(numbers):
                if sum == target: #타겟 넘버 만드는 방법의 수 증가
                    answer += 1
                return
        dfs(n+1,sum+numbers[n], numbers, target) #먼저 하나씩 더한다
        dfs(n+1,sum-numbers[n], numbers, target) #다음에 하나씩 뺀다
    
    answer = 0
    dfs(0,0,numbers,target)
    
    return answer




