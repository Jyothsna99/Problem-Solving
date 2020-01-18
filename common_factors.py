"""Eg:factors of 12 are 1,2,3,4,6,12
factors of 10 are 1,2,5,10
Common factors are 1,2"""
import math
n=[int(x) for x in input().split()]
g=math.gcd(n[0],n[1])
count=1
for i in range(2,g+1):
    if n[0]%i==0:
        count+=1
print(count)

    