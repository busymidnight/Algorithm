import re

def solution(files):
    # 숫자를 기준으로 split
    temp = [re.split("([0-9]+)", s) for s in files]

    # 첫 번째 요소가 같은 경우 두 번째 요소를 int로 변환하여 비교
    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]