n , m = map(int,input().split())
box = [0]*n
for idx in range(n):
    box[idx] = idx+1
for _ in range(m):
    i ,j = map(int,input().split())
    box[i-1], box[j-1] = box[j-1], box[i-1]

for i in range(n):
    print(box[i], end=' ')