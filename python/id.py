
n=str(input('enter student id:'))
if n[0:2].isalpha():
                            print("invalid")
elif n[2:5].isdigit():
                            print("invalid")
elif n[5:9].isalpha():
                             print("invalid")
elif len(n)!=9:
    print('invalid')
else:
        print("valid")


