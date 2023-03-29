max = 0
max_idx = 0
for i in range(0, 9):
    n = int(input())
    if max == 0:
        max = n
        max_idx = i
    else:
        if n > max:
            max = n
            max_idx = i
print(max)
print(max_idx+1)
