n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
print(f"{n_list[0]} {n_list[n-1]}")