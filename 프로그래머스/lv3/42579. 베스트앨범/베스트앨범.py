def solution(genres, plays):
    answer = []
    hash = {}
    for i, (g,p) in enumerate(zip(genres,plays)):
        if g in hash.keys():
            hash[g] = [hash[g][0]+p, hash[g][1]+[[p,i]]]
        else:
            hash[g] = [p, [[p,i]]]
    for _, indexs in sorted(hash.items(), key= lambda x:-x[1][0]):
        for index in sorted(indexs[1], key= lambda x:-x[0])[:2]:
            answer.append(index[1])
    return answer