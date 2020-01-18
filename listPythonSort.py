l=[int(x) for x in input().split()]
if(all(l[i] < l[i+1]  for i in range(len(l)-1))):
    print("List is sorted in ascending order")
elif(all(l[i] > l[i+1]  for i in range(len(l)-1))):
    print("List is sorted in descending order")
else:
    print("List is not sorted")