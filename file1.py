fo = open('D:/Ann/abc.txt', "r+")
print("Name of the file: ",fo.name)
hi = "hello python is fun for everyone"
fo.write(hi)
str = fo.read(50)
print("the read string is\n", str)
fo.close()
