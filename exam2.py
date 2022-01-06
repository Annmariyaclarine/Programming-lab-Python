def fibo(n):
	a=0
	b=1
	if(n<=0):
		print("Enter a positive integer")
	elif(n==1):
		print(0)
		
	else:
		i=2
		print(0)
		print(1)
		while(i<n):
			c=a+b
			print(c)
			a=b
			b=c
			i=i+1
N=int(input("Enter the number of terms N :"))
fibo(N)

			
			