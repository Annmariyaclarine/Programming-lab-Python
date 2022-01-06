def fact(n):
	f=1
	if(n==1):
		print("factorial= 1")
	else:
		for i in range(1,n+1):
			f=f*i
		print("Factorial= ",f)
num=int(input("Enter the number"))
if(num==0):
	print("factorial= 1")
else:
	fact(num)