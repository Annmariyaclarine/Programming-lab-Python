list=[]
m=int(input("The max size of list"))
for i in range(m):
	e=int(input("enter the element"))
	list.append(e)
N=int(input("Enter the position upto where square is to be calculated "))
for i in range (N):
	list[i]=list[i]**2
	print(list[i])
