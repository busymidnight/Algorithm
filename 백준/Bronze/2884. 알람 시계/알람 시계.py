H, M = map(int,input().split())
time = H * 60 + M - 45
H = time //60
M = time % 60
if H < 0:
    H += 24
if M < 0:
    M += 60
print(f"{H} {M}")