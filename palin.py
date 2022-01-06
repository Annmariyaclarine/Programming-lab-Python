def palindrome(n):
	s=0
	temp=n
	while(n>0):
		rem=n%10
		s=s*10+rem
		n=n//10
	print(s)
	if(s==temp):
		print("YES")
	else:
		print("no")
n=int(input("NUM : "))
palindrome(n)
