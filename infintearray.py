T=int(input())
n=int(input())
a=[int(x) for x in input().split()]
q=int(input())
l=[int(x) for  x in input().split()]
r=[int(x) for x in input().split()]
o=[]
s=0
for i in range(len(l)):
    for j in range(l[i],r[i]+1):
        if j>len(a):
            j=j%len(a)
        s+=a[j-1]
    o.append(s)
    s=0
print(*o)
print("length of b is",max(r))
    