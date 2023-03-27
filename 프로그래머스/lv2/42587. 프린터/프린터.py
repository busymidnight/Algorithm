from collections import deque
def solution(priorities, location):
    dq = deque(priorities)
    doc = [0 for _ in range(len(priorities))]
    doc[location] = 1
    dq_doc = deque(doc)
    answer,cnt = 0, 0
    
    while(dq_doc):
        priority = dq.popleft()
        check_doc = dq_doc.popleft()
        if len(dq) > 1 and max(dq)> priority:
            dq.append(priority)
            dq_doc.append(check_doc)
        else:
            cnt+=1
            if check_doc == 1:
                answer = cnt
                break
    return answer