def conv(n):
	sum=0
	rem=0
	while(n>0):	
		rem=n%10
		sum=sum+rem*2**i
		n=n//10
		i=i+1
	print("decimal num:",sum)

	

n=int(input("Enter the binary number to be converted"))