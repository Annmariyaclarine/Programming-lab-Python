print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Select choice"))
if choice==1:
	a=float(input("Enter first num"))
	b=float(input("Enter second num"))
	c=a+b
	print("sum is=",c)
elif choice==2:
	a=float(input("Enter first num"))
	b=float(input("Enter second num"))
	c=a-b
	print("difference is=",c)
elif choice==3:
	a=float(input("Enter first num"))
	b=float(input("Enter second num"))
	c=a*b
	print("product is=",c)
elif choice==4:
	a=float(input("Enter first num"))
	b=float(input("Enter second num"))
	c=a/b
	print("quotient is=",c)
else:
	print("Wrong choice")

