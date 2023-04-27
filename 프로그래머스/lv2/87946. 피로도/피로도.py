answer = 0
def dfs(k, cnt, dungeons, check):
    global answer
    answer = max(cnt, answer)
    
    for i in range(len(dungeons)):
        if check[i] == 0 and k >= dungeons[i][0]: #방문한적 없고 최소피로도가 K보다 작거나 같은 던전
            check[i] = 1
            dfs(k-dungeons[i][1], cnt+1, dungeons, check)
            check[i] = 0
            
def solution(k, dungeons):
    global answer
    check = [0] * len(dungeons) #방문 체크
    dfs(k, 0, dungeons, check)
    return answer