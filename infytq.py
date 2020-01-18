mil=int(input("Enter mileage"))
amnt=int(input("Enter amount per 1 litre of fuel"))
dis=int(input("Enter distance"))
tot=((dis*2)/mil)*amnt;
print(tot/4)
if tot%5==0:
    print("True")
else:
    print("False")
    