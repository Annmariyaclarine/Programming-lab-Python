def fac(n):
	if(n==1):
		return 1
	else:
		f=n*fac(n-1)
		return f
num=int(input("Enter the number"))
if(num<0):
	print("Factorial doesn't exist")
elif(num==0):
	print("Factorial= 1")
else:
	print("Factorial= ",fac(num))