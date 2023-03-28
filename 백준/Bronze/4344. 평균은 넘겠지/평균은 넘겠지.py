n = int(input()) #test case
for _ in range(n):
    std_list = list(map(int, input().split()))
    stdnum = std_list[0]
    sum_std = sum(std_list) - stdnum
    avg = sum_std/stdnum
    cnt = 0
    for i in range(1,stdnum+1):
        if std_list[i] > avg:
            cnt += 1
    percent = cnt/stdnum*100
    print(format(percent,".3f")+"%")