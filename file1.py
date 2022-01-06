fo = open('D:/Ann/abc.txt', "r+")
print("Name of the file: ",fo.name)
hi = "hellopython is fun for everyone"
fo.write(hi)
str = fo.read(50)
print("the read string is\n", str)
# Close the opened file
fo.close()