jl=int(input("Enter job level"))
sal=int(input("Enter current salary"))
if jl==3:
    print(sal+(sal*15/100))
elif jl==4:
    print(sal+(sal*7/100))
elif jl==5:
    print(sal+(sal*5/100))
else:
    print(sal)