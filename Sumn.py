def sum1(n):
	sumn=0
	for i in range(1,n+1):
		sumn=sumn+i
		i=i+1
	return(sumn)
n=int(input("Enter the number"))
print("Sum of numbers upto ",n," is : ",sum1(n))
