a=(input("enter first string:"))
b=(input("enter second string:"))
cnt=0
temp=0
for word in a:
                    cnt=cnt+1
for word in b:           
                    temp=temp+1
if cnt>temp:
                    print("first string is bigger")
else:
                     print("second is bigger")   
