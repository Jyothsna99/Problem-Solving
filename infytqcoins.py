one=int(input("Enter available number of one rupee coins"))
five=int(input("Enter available number of five rupee coins" ))
amnt=int(input("Enter amount"))
e=0
rfive=amnt//5
rone=amnt-(rfive*5)
if rfive>five:
    e=rfive-five
    rfive=rfive-e
    rone=amnt-(rfive*5)
if rone>one:
    print(-1)
else:
    print("NO of 1 rupee coins",rone)
    print("No of 5 rupee coins",rfive)