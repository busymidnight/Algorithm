def solution(s):
    answer = set()
    result = []
    elems = s[2:-2]
    elems=elems.split("},{")
    elems.sort(key=lambda x : len(x))
    for elem in elems:
        temp = set(list(map(int, elem.split(','))))
        result = result + list(set.difference(temp, answer))
        answer=temp
    return result