def add(a,b):
	c=a+b
	print(c)
def sub(a,b):
	c=a-b
	print(c)
def multi(a,b):
	c=a*b
	print(c)
def divi(a,b):
	if(b==0):
		print("Division by Zero not possible")
	else:
		c=a/b
		print(c)
def pow(a,b):
	c=a**b
	print(c)
def rem(a,b):
	if(b==0):
		print("Division by Zero not possible")
	else:
		c=a%b
		print(c)
while(True):
	print("Select from the given options")
	print("1.Addition   2.Subtraction   3.Multiplication   4.Division    5.Exponent  6.Modular division  7.Exit")
	choice=int(input("Enter the choice: "))
	if(choice==1):
		print("ADDITION")
		a=float(input("Enter first number:")) 
		b=float(input("Enter second number:")) 
		add(a,b)
	elif(choice==2):
		print("SUBTRACTION")
		a=float(input("Enter first number:")) 
		b=float(input("Enter second number:")) 
		sub(a,b)
	elif(choice==3):
		print("MULTIPLICATION")
		a=float(input("Enter first number:")) 
		b=float(input("Enter second number:")) 
		multi(a,b)
	elif(choice==4):
		print("DIVISION")
		a=float(input("Enter dividend:")) 
		b=float(input("Enter divisor:")) 
		divi(a,b)
	elif(choice==5):
		print("EXPONENT")
		a=float(input("Enter  number:")) 
		b=float(input("Enter power:")) 
		pow(a,b)
	elif(choice==6):
		print("MODULAR DIVISION")
		a=float(input("Enter dividend:")) 
		b=float(input("Enter divisor:")) 
		rem(a,b)
	elif(choice==7):
		print("EXIT")
		break
	else:
		print("WRONG CHOICE !!")
		print("Enter correct choice")