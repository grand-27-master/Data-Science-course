j=0
i=0
n=int(input("enter rows="))
for i in range(n):
                            print()
                            for j in range(i+1):
                                                                    print(2**j,end=' ')
                            for j in range(i-1,-1,-1):   
                                                                    print(2**j,end=' ')
                            
