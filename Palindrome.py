def palindrome(n):
	s=0
	temp=n
	while(n!=0):
		rem=n%10
		s=s*10+rem
		n=n//10
	print(s," is the reverse of number")
	if(temp==s):
		print(temp," is palindrome")
	else:
		print("So, ",temp," is not palindrome")
n=int(input("NUM : "))
palindrome(n)
