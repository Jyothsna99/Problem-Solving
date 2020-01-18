'''eg:((2))(3) Output:True
EG:(((2))) Output:False'''
n=input()
l=[y for x in n.split('(') for y in x.split(')') if y!=""]
count=0
flag=0
for i in n:
    if i in l:
        if count==int(i):
            flag+=1
    else:
        if i=='(':
            count+=1
        else:
            count-=1
if flag==len(l):
    print("True")
else:
    print("False")