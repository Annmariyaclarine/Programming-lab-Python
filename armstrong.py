n=int(input("Enter the number"))
temp1=n
temp2=n
s=0
while(n!=0):
	s=s+1
	n=n//10
print("No of digits=",s)
rs=0
while(temp2!=0):
	r=temp2%10
	rs=rs+r**s
	temp2=temp2//10
if(rs==temp1):
	print(rs,"is an armstrong number")
else:
	print("not an armstrong number")
