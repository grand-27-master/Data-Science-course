n=int(input())
s=[]
for i in range(0,n):
    s.append(input())
for i in range(0,n):
    c=''
    d=''
    for j in range(0,len(s[i])):
        if(j%2==0):c+=s[i][j]
        else:d+=s[i][j]
    print(c,d)
