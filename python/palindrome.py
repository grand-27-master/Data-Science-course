n=int(input('enter number='))
tot=0
rem=0
temp=n
while(n>0):
    rem=n%10
    tot=tot*10+rem
    n=int(n/10)
n=temp
#print('palindrome number=',n)
if temp==tot:
    print(n,'is a palindrome number')
else:
    print(n,'is not a palindrome number')
