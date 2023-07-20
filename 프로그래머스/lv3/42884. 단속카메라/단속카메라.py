def solution(routes):
	# 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    # 진입 지점의 최솟값이 기준
    key = -30001
    cnt = 0
    
    for route in routes:
    	# 기준(카메라)보다 진입지점이 뒤에 있으면
        if route[0] > key:
        	# 단속이 안되기에 카메라 하나 더 필요
            cnt += 1
            # 새로운 기준은 해당 경로의 진출지점
            key = route[1]
            
    return cnt