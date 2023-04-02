dic = {
    'ABC' : 2,
    'DEF' : 3,
    'GHI' : 4,
    'JKL' : 5,
    'MNO' : 6,
    'PQRS' : 7,
    'TUV' : 8,
    'WXYZ' : 9
}


dials = input()
sum = 0
for dial in dials:
    for k in dic.keys():
        if dial in k:
            sum += int(dic[k])+1
           
print(sum)