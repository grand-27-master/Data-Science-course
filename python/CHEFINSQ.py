#chef and its consequences


from math import factorial as facto
for f in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split())
    h_array=[for i in range(0,100)]
for i in l:
    h_array[i]+=1
r=0
for j in h_array:
    if j<b:
        j-=b
    elif b<=0:
        break
    else:
        r=facto(j)/(facto(b)*facto(b-j))
        b-=j
print(int(r))        
