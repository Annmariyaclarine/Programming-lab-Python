n=int(input("Enter the num of rows"))
for i in range(1,n+1):
	print("\t")
	for j in range(1,i+1):
		print(i*j,end=" ")

	print(" ")