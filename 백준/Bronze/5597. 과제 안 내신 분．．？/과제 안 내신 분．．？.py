std = [i for i in range(1,31)]
for i in range(28):
    data = int(input())
    std.remove(data)
print(min(std))
print(max(std))