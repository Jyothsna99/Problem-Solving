s=input()
maxlength=1
for i in range(1,len(s)):
    low=i-1
    high=i
    while low>=0 and high<len(s) and s[low]==s[high]:
        if high-low+1>maxlength:
            start=low
            maxlength=high-low+1
        low-=1
        high+=1
    low=i-1
    high=i+1
    while low>=0 and high<len(s) and s[low]==s[high]:
        if high-low+1>maxlength:
            start=low
            maxlength=high-low+1
        low-=1
        high+=1
print("longest palindrome in a given string is:",s[start:start+maxlength])
print("length=",maxlength)