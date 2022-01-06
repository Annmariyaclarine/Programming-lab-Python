def conv(n):
	s=0
	rem=0
	i=0
	while(n>0):	
		rem=n%10
		s=s+rem*(2**i)
		n=n//10
		i=i+1
	print("decimal num:",s)	
n=int(input("Enter the binary number to be converted"))
conv(n)
