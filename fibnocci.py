def fib(n):
	a=0
	b=1
	for i in range(0,n):
		f=a+b
		print(f)
		a=b
		b=f
		
		
n=int(input("Enter the Number: "))
if(n==0):
	print(0)
elif(n==1):
	print(0,1)
else:
	print(0)
	print(1)
	fib(n)