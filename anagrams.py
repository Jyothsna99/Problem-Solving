t=int(input())
s=[]
c=[]
for i in range(2*t):
    if i%2==0:
        s.append(input())
    else:
        c.append(input())
for i in range(t):
    s1=s[i]
    s2=c[i]
    count=0
    l=len(s2)
    for j in range(len(s1)+1-l):
        if sorted(s1[j:j+l])==sorted(s2):
            count+=1
    print(count)