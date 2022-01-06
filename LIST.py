list=[]
m=int(input("max size"))
for i in range(0,m):
     e=int(input("enter"))
     list.append(e)
N=int(input ("enter n"))
for i in range(N):
    list[i]=list[i]**2
    print(list[i])