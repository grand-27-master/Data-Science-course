
#cnt=1
#n=int(input("enter number="))
#i=n
#while i>=1:
 #   cnt=cnt*i
  #  i=i-1
#print(cnt)
    

n=int(input('enter number='))
def fact(n):
    cnt=1
    for i in range(n,0,-1):
        cnt=cnt*i    
    return cnt
print('answer=',fact(n))    
        




