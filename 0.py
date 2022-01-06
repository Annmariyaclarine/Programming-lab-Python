a=int(input("first"))
b=int(input("second"))
c=int(input("third"))
if(a>b and a>c):
	l=a
elif(b>a and b>c):
	l=b
else:
	l=c
print(l)
