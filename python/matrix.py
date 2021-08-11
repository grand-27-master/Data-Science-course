a=int(input('enter rows='))
b=int(input('enter columns='))
l=[]                                    #taking blank list 
print('enter elements to be entered:')
for i in range(1,a):
    m=[]                                #list to be appended
    for j in range(1,b):
        m.append(int(input()))
    l.append(m)    
print(l)

 #sum of diagonal elements

s=0
for i in range(1,a):
    for j in range(1,b):
        if(i==j):
            s=s+l[i][j]
print("\n Sum of diagonal elements are: ",s)
            

             
