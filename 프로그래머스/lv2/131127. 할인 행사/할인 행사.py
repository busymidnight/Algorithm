from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    
    #10일 동안만 회원 자격을 부여하기 때문에 10일씩 비교
    #discount의 최솟값은 10이므로 -9를 해줘야 최소 1번 반복 가능하다.
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == check:
            answer += 1

    return answer