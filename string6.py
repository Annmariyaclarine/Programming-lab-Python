list=[]
n=int(input("Enter the number of words:"))
for i in range(0,n):
	word=input("Enter the word: ")
	list.append(word)
max_length=len(list[0])
temp=list[0]
for i in list:
	if(len(i)>max_length):
		max_length=len(i)
		temp=i
print("Longest word: ",temp)
print("Length of longest word ",temp," is :",max_length)