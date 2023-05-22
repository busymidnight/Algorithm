def solution(numbers, target):

    def dfs(n, sum, numbers,target):
        nonlocal answer
        if n == len(numbers):
                if sum == target:
                    answer += 1
                return
        dfs(n+1,sum+numbers[n], numbers, target)
        dfs(n+1,sum-numbers[n], numbers, target)
    
    answer = 0
    dfs(0,0,numbers,target)
    
    return answer




