import math
def solution(fees, records):
    # fees: [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
    # 요금 계산: 기본 요금 + ((누적 주차 시간 - 기본 시간)/단위 시간)의 올림 * 단위 요금
    # records: ["시간, 차번호, 인아웃", " , , ", ...]
    dic = {}

    for record in records:
        time, number, inout = record.split()
        time = time.split(':')
        #시간 계산(분으로)
        time = int(time[0])*60 + int(time[1])
        
        if number not in dic:
            dic[number] = (0, time, inout) #처음 
        if inout == 'IN':
            dic[number] = (dic[number][0], time, inout) #입차
        elif inout == 'OUT':
            total_time, in_time, _ = dic[number] #출차
            total_time += time - in_time
            dic[number] = (total_time, time, inout)

    result = {}

    for number in dic.keys():
        total_time, time, inout = dic[number]
        if inout == 'IN':
            total_time += 1439 - time #23시59분 출차라고 치고 계산
        fee = fees[1]
        if total_time <= fees[0]:
            result[number] = fee
        else:
            fee = fee + math.ceil((total_time - fees[0]) / fees[2]) * fees[-1]
            result[number] = fee

    return list(map(lambda x : x[1], sorted(result.items())))