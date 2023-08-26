def solution(msg):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    cnt = 27
    search = ''
    #사전 초기화
    dic = {k:v for k,v in zip(alphabet, range(1,27))}
    
    while i<len(msg):
        search += msg[i]
        if search in dic:
            i += 1
            continue
        else:
            dic[search] = cnt
            cnt += 1
            
            s = search[:-1]
            answer.append(dic[s])
            search = ''
            
    answer.append(dic[search])
    return answer