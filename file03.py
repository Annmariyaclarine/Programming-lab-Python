fn=open('D:/Ann/test.txt','r')
fn1=open('newfile.txt','w+')
cont=fn.readlines()
print(cont)
print("LEN=",len(cont))
for i in range(0,len(cont)):
    print("i=",i)
    if(i%2==0):
	    fn1.write(cont[i])
	    print(cont[i])
    else:
	    continue
fn1.close()
fn1=open('newfile.txt','r')
print(fn1.read())
fn1.close()
