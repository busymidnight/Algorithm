n, x = map(int, input().split())
listA = list(map(int, input().split()))
listB = []
for a in listA:
    if a<x:
        listB.append(a)
print(*listB)