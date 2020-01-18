l=[]
n=int(input())
for i in range(n):
    a=[int(x) for x in input().split()]
    l.append(a)
k=[y for x in l for y in x]
k=sorted(set(k))
for i in range(n):
    for j in range(n):
        l[i][j]=k.index(l[i][j])+1
print(l)