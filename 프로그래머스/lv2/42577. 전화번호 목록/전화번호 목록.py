def solution(phone_book):
    hash_map = {}
    # 전화번호 목록을 해시 테이블에 저장
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    
    # 각 전화번호의 접두어가 해시 테이블에 있는지 확인
    for phone_number in phone_book:
        prefix = ""
        for digit in phone_number:
            prefix += digit
            if prefix in hash_map and prefix != phone_number:
                return False
    return True
