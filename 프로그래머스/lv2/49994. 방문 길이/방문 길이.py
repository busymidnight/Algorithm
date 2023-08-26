def solution(dirs):
    answer = 0
    x,y = 5, 5
    # 'U', 'D', 'R', 'L'
    Map = []
    move = {'U':(0,1),'D':(0,-1),'R':(1,0),'L':(-1,0)}
    for i in range(len(dirs)):
        (dy,dx) = move[dirs[i]]
        if not (0 <= x+dx and x+dx <=10 and 0<=y+dy and y+dy<=10):
            continue
        Map.append((x,y,x+dx,y+dy)) 
        Map.append((x+dx,y+dy,x,y)) #양방향 체크, 예를 들어 왼->오/오->왼은 중복이므로 추후에 중복 제거를 위해 양방향을 다 기록해둔다.
        x = x + dx
        y = y + dy
    #중복 원소 제거
    mapSet = set(Map)
    answer=len(mapSet)//2

    return answer