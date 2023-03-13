import math
def solution(arr):
    lcm = arr[0] * arr[1] // math.gcd(arr[0],arr[1])
    for i in range(1,len(arr)-1):
        lcm = lcm * arr[i+1] // math.gcd(lcm,arr[i+1])
    return lcm