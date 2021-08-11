c1=eval(input("enter cost of one PC="))
n1=eval(input("no.of PCs="))
cost_computers=n1*c1
print("cost of computers=",cost_computers )
c2=eval(input("enter cost of one chair="))
n2=eval(input("no. of chairs="))
c3=eval(input("enter cost of one table="))
n3=eval(input("no. of tables="))
cost_ furniture=n3*c3+n2*c2
print("cost of furniture=",cost_furniture)
n4=int(input("no. of hours worked="))
w=int(input("wages per hour=") )
cost_labour=w*n4
print("cost of labour",cost_labour)
budget_lab=cost_computers+ cost_furniture+cost_labour
print("budget of the lab=",budget_lab)
     
