a=input("Enter string:")
print(a,"IS THE GIVEN STRING")
print(len(a))
print("The characters in the string are:")
for i in range(0,len(a)):
	print(a[i])
print("The characters in the revrese order of the string are:")
for i in range(len(a)-1,-1,-1):
	print(a[i])