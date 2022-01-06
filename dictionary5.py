import csv
csv_columns=['id','column1','column2','column3','column4','column5']
dict_data={'id':['1','2','3'],
	'column1':[33,25,56],
	'column2':[35,30,30],
	'column3':[21,40,55],
	'column4':[71,25,55],
	'column5':[10,10,40],}
csv_file="temp.csv"
try:
	with open(csv_file,'w') as csvfile:
		writer=csv.DictWriter(csvfile,fieldnames=csv_columns)
		writer.writeheader()
		writer.writerow(dict_data)
except IOError:
	print("I/O error")
data=csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data:
	print(row)
