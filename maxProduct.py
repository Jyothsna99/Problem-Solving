'''find the sequence from the array such that the product is maximum'''
a=[-1,-2,3,0,7,-8,-9]
max_end_here=1
min_end_here=1
max_so_far=1
flag=0
for i in range(len(a)):
    if a[i]>0:
        max_end_here*=a[i]
        min_end_here=min(min_end_here*a[i],1)
        flag=1
    elif a[i]==0:
        max_end_here=1
        min_end_here=1
    else:
        temp=max_end_here
        max_end_here=max(min_end_here*a[i],1)
        min_end_here=temp*a[i]
    if max_so_far<max_end_here:
        max_so_far=max_end_here
if max_so_far==1 and flag==0:
    print(0)
else:
    print(max_so_far)
