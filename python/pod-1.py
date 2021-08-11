

#For example, consider the number  8975.
#The sum of the digits that occur in the alternate positions from the first position
#is 8+7=15.
#The sum of the digits that occur in the alternate positions,
#starting from the rightmost position is 5+9 = 14.
#Difference between the two sums is 1 (=15-14).
#Similarly, for the number 5798, the difference between  two sums, is 1.  




n=str(input('enter number='))
if len(n)!=4:
    print('invalid')
for i in range(0,len(n)):
    
