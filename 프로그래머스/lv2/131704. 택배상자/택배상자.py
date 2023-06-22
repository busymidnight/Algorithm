def solution(order):
    side_container = []
    current = 0
    i = 1 
    while i != len(order) + 1:
        side_container.append(i)
        while side_container[-1] == order[current]:
            current += 1
            side_container.pop()
            
            if len(side_container) == 0:
                break
        i += 1
    return current