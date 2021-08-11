# f1=open('file2.txt','r')
# print('i am python',f1.tell())
# f1.close()


fh = open('hello.txt', 'w+')
print(fh.write("sample text"))
fh.close()
