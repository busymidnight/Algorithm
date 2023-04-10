n = int(input())
for i in range(1,n):
   answer=(2*i-1)*"*"
   print(" "*(n-i)+answer)
for i in range(n,0,-1):
   answer=(2*i-1)*"*"
   print(" "*(n-i)+answer)