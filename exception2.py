while True:
	print("DIVISION")
	a=float(input("enter the dividend:"))
	b=float(input("enter the divisor:"))
	if(b==0):
		raise Exception("Sorry, Divison by zero is not defined")
	c=a/b
	print(a,"/",b,"=",c)