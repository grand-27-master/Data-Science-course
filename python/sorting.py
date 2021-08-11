#bubble sort


l=[3,4,1,2,5]
for i in range(0,len(l)):
    for j in range(1,len(l)):
        if (l[j-1]>l[j]):
            l[j-1],l[j]=l[j],l[j-1]
print('sorted order=',l)            


