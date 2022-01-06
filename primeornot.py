n=int(input("Enter the number"))
if(n>2):
	for i in range(2,n):
		if(n%i==0):
			print("Not prime number")
			break
	else:
		print("Prime number")
elif(n==2):
	print("Prime")
else:
	print("Not Prime number")


	

	