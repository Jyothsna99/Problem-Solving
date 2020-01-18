'''eg:(([]{[]})) output:True
    (){}[{] output:False'''
s=input()
l=['()','[]','{}']
while any(x in s for x in l):
    for i in l:
        s=s.replace(i,"")
if s=="":
    print("True")
else:
    print("False")