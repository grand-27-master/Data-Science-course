print("**********CALCULATOR**********")

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("Select your choice:")
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Division")

choice=input("enter choice 1/2/3/4:")
n1=int(input("enter first number="))
n2=int(input("enter second number="))

if choice=='1':
    print("answer=",add(n1,n2))
elif choice=='2':
    print("answer=",sub(n1,n2))
elif choice=='3':
    print("answer=",mul(n1,n2))
elif choice=='4':
    print("answer=",div(n1,n2))

else:
    print('invalid input')




    
