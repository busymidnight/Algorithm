n ,m = map(int, input().split())
box = [i+1 for i in range(n)]
for _ in range(m):
    i, j =map(int, input().split())
    boxes = box[i-1:j]
    boxes.reverse()
    box[i-1:j] = boxes
print(*box)