def solution(numbers):
    #
    numbers = list(map(str, numbers))
    
    # 세자리 수 이상으로 자릿수를 맞추어 아스키 코드에 따라 정렬
    # ex) 333 303030 343434 
    # 앞에서부터 세자리로 잘라서 비교하면 30보다 3이 앞에 가야함
    # 네번째 자릿수부터의 수로 인한 정렬의 변화는 의미없음. 
    # 네번째 자릿수가 정렬에 영향을 미친다는 것은 세번째 자릿수까지의 수가 서로 같다는 뜻인데, 
    # 이 때는 실제로는 둘 다 같은 수 취급이므로 어떻게 정렬되든 상관없기 때문
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    # [0,0,0]의 경우를 생각하여 int 변환이 있어야함
    return str(int(''.join(numbers)))