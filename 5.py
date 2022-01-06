n=int(input("Enter rows"))
for i in range(1,n+1):
	print("\t")
	for j in range(1,i):
		print("*",end="  ")
	print(" ")
for i in range(n,0,-1):
	print("\t")
	for j in range(i):
		print("*",end="  ")
	print(" ")
