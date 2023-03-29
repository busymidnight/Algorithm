num_list = [0]*10
for i in range(10):
    num = int(input())
    num_list[i] = num%42
print(len(set(num_list)))
