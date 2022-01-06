str=input("Enter a string:")
str=str.casefold()
rev=reversed(str)
if(list(str)==list(rev)):
	print("Palindrome")
else:
	print("Not Palindrome")