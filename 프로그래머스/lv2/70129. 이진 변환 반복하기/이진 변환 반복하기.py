def solution(s):
    cnt = 0
    zerocnt = 0
    while s != '1':
        zerocnt += s.count("0")
        s = s.replace("0","")
        num = len(s)
        s = bin(num)[2:]
        cnt += 1
        
    return [cnt, zerocnt]