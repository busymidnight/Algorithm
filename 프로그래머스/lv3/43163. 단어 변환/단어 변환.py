from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0   
    q = deque()
    q.append([begin, 0])    
    while q:
        a, cnt = q.popleft()
        if a == target:
            return cnt
        for i in range(len(words)):
            temp = 0
            word = words[i]
            for j in range(len(a)):
                if a[j] != word[j]:
                    temp += 1
            if temp == 1:
                q.append([word, cnt+1])
    return 0