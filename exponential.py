def facto(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return(f)
x=int(input("Enter x: "))
n=int(input("Enter n: "))
ex=1
for i in range(1,n+1):
	ex=ex+((x**i)/(facto(i)))
print(ex)