num1=float(input("Enter 1st "))
num2=float(input("Enter 2nd "))
num3=float(input("Enter 3rd "))
if(num1>num2)and(num1>num3):
	largest=num1
elif(num2>num1)and(num2>num3):
	largest=num2
else:
	largest=num3
print("Largest num : ",largest)