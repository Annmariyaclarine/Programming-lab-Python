w=input('Enter the string:')
a=[]
str=w.split()
for i in str:
    print(i," ")
    if i not in a:
        a.append(i)
print("List",a)
count=0
for i in range(len(w)):
    if(w[i]=='a'):
        count=count+1
print("The occurrence of a : ", count)
