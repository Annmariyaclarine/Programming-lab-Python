def sumof(n):
	sum1=0
	digit=0
	temp=n
	while(n!=0):
		n=n%10
		sum1=sum1+n
		digit=digit+1
		temp=temp//10
	print("sum is=",sum1,"no of digits=",digit)
n=int(input("Enter the number"))
sumof(n)
