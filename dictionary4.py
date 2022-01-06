n=int(input("Enter the number of students"))
studlist=[]
for i in range(0,n):
	stud={}
	stud["name"]=input("Enter the name")
	stud["roll"]=int(input("Enter the roll number"))
	stud["attendence"]=int(input("Enter the attendence percentage:"))
	studlist.append(stud)

for i in range(1,n):
	for j in range(0,n-1):
		if(studlist[j]["attendence"]<studlist[j+1]["attendence"]):
			temp=studlist[j]
			studlist[j]=studlist[j+1]
			studlist[j+1]=temp
print("Attendance list")
for i in range(0,n):
	print(studlist[i])