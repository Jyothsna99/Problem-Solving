'''Given a 2D array of digits or grid, try to find the occurrence of a given 2D pattern of digits. For example, consider the following grid:

1234567890  
0987654321  
1111111111  
1111111111  
2222222222  
Assume we need to look for the following 2D pattern array:

876543  
111111  
111111
The 2D pattern begins at the second row and the third column of the grid. The pattern is said to be present in the grid.

Function Description

Complete the gridSearch function in the editor below. It should return YES if the pattern exists in the grid, or NO otherwise.

gridSearch has the following parameter(s):

G: the grid to search, an array of strings
P: the pattern to search for, an array of strings
Input Format

The first line contains an integer , the number of test cases.

Each of the  test cases is represented as follows:
The first line contains two space-separated integers  and , indicating the number of rows and columns in the grid .
This is followed by  lines, each with a string of  digits representing the grid .
The following line contains two space-separated integers,  and , indicating the number of rows and columns in the pattern grid .
This is followed by  lines, each with a string of  digits representing the pattern .

Output Format

Display YES or NO, depending on whether  is present in .
'''

import os
# Complete the gridSearch function below
def gridSearch(G, P):
    j=0
    index=[]
    l=0
    start=0
    #this for loop is for finding the first row of P in G and find all the indices of pattern p[0] in G  
    for i in range(len(G)):
        if P[j] in G[i]:
            start=i
            s=G[i].find(P[j])
            index.append(s)
            for k in range(s+1,len(G[i])):
                pos=G[i].find(P[j],k)
                if pos>=0:
                    index.append(pos)
            l+=1
            j+=1
            break
    else:
        return "NO"
    j=start+1
    
    #this is to check the grid in all the indices find above
    for ind in index:
        j=start+1
        for k in range(1,len(P)):
            if ind+len(P[k])>len(G[j]):
                return "NO"
            temp=G[j][ind:ind+len(P[k])+1]
            if temp.find(P[k])==0:
                l+=1
                j+=1
            else:
                l=1
                break
        if l==len(P):
            break
    if l==len(P):
        return "YES"
    #if the pattern not found then G matrix sinks to the next row of the start index and recursively call the gridSearch function
    else:
        if start>=len(G):
            return "NO"
        G=G[start+1:]
        return gridSearch(G,P)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
