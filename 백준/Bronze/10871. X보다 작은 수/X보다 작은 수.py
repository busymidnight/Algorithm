nx = list(map(int, input().split()))
listA = list(map(int, input().split()))
listB = []
for a in listA:
    if a<nx[1]:
        listB.append(a)
print(*listB)