str=input("Enter the string:")
c=input("Enter the character:")
count=0
for i in range(len(str)):
	if(str[i]==c):
		count=count+1
print(count)