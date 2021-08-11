a=int(input('enter first number='))
b=int(input('enter second number='))
if ((a%2==0 and b%2!=0) or (a%2!=0 and b%2==0)):
    print('LCM=',a*b)
elif a%2!=0 and b%2!=0:
    print('LCM=',max(a,b))

elif a%2==0 and b%2==0:
    print('LCM=',max(a,b))    
