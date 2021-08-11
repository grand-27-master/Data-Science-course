'''***input value inside class***
class demo:
    a=10

    def obj(self):
        print(self.a)             #self acts as this function as in java

d=demo()                          #defining object
d.obj()                           #calling function using object




input value outside class
class demo:

    def __init__(self,a,b):       #used to initialise variable
        self.a=a
        self.b=b

    def obj(self):
        print("values of a=",self.a)
        print("values of b=",self.b)



d1=demo(1,2)
d1.obj()
d2=demo(3,4)
d2.obj()
'''
