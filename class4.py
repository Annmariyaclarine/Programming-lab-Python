class Time:
	def __init__(self, hours, mins, sec):
		self.hours = hours
		self.mins = mins
		self.sec = sec
	def __add__(t1, t2):
		t3 = Time(0, 0, 0)
		if t1.mins + t2.mins > 60:
			t3.hours = (t1.mins + t2.mins) // 60
		t3.hours = t3.hours + t1.hours + t2.hours
		t3.mins = (t1.mins + t2.mins) % 60
		t3.sec = (t1.sec + t2.sec)
		return t3
	def displayTime(self):
 		print("Time is ", self.hours, "hours ", self.mins, "minutes", "and", self.sec,"seconds")
	def displayMinute(self):
		print("minutes:", self.hours * 60 + self.mins)
	def displaysecond(self):
		print("second:", self.hours * 60 * 60 + self.mins * 60 + self.sec)
h1 = int(input("enter time 1 hour:"))
m1 = int(input("enter time 1 minutes:"))
s1 = int(input("enter time 1 second:"))
h2 = int(input("enter time 2 hour:"))
m2 = int(input("enter time 2 minutes:"))
s2 = int(input("enter time 2 second:"))
a = Time(h1, m1, s1)
b = Time(h2, m2, s2)
c = a + b
c.displayTime()
c.displayMinute()
c.displaysecond()