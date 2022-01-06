a=int(input("Enter the size of array"))
m=[]
for i in range(a):
	ele=int(input("Enter the element"))
	m.append(ele)
print("The array is")
for i in range(0,a):
	print(m[i])
temp=0
for i in range(0,a):
	for j in range(i,a):
		if(m[i]>m[j]):
			temp=m[i]
			m[i]=m[j]
			m[j]=temp
print("The largest number is",m[a-1])
