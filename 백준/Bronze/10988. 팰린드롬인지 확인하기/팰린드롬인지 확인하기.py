from collections import deque
s=list(input())
dq = deque(s)
def find(dq):
    while len(dq)>1:
        if dq[0] == dq[-1]:
            dq.popleft()
            dq.pop()
        else:
            print("0")
            return 
    print("1")
find(dq)