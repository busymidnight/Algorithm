N, M = map(int,input().split())
array = [i for i in range(1,N+1)]

for i in range(M):
    begin, end, mid = map(int,input().split())
    for j in range(mid-begin):
        array.insert(end,array[begin-1])
        array.remove(array[begin-1])

print(*array)