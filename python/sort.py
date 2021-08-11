b=[1,3,4,2,6]
def bubble(b):
    l=len(b)
    while l>1:
        i=1
        while i<l:
            if b[i]<b[i-1]:
                swap(b,i,i-1)
        i+=1
    l-=1
a=bubble(b)
print(a)
