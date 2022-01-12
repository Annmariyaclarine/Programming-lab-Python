class rect:
	def __init__(self, a, b):
		self.length = a
		self.breadth = b
	def area(self):
		return self.length * self.breadth
	def __lt__(self, o):
		if self.area() < o.area():
			return True
		else:
			return False
h1 = int(input("enter length of first rectangle:"))
b1 = int(input("enter breadth of first rectangle:"))
h2 = int(input("enter length of second rectangle:"))
b2 = int(input("enter breadth of second rectangle:"))
rect1 = rect(h1, b1)
rect2 = rect(h2, b2)
if rect1 < rect2:
	print("rectangle 2 is greater than rectangle 1")
else:
	print("rectangle 1 is greater than rectangle 2")