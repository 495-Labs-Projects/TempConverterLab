'''
Jordan Stapinski
67-495 Temperature Converter Lab (Object-Oriented Version)

Python equivalent of 67-272 lab 2: Temperature Converter

NOTE: python3 -m py_compile <THIS_FILENAME> will compile but not run the script
'''

class TempConverter(object):
	def __init__(self, temp, measure="F"):
		self.temp = temp
		self.measure = measure

	def convert(self):
		if type(self.temp) != int:
			return "Temperature must be an integer"
		if self.is_below_absolute_zero():
			return "Temperature below Absolute Zero"
		if (self.measure == "F"):
			return 5 * (self.temp - 32)/9
		if (self.measure == "C"):
			return (9 * self.temp)/5 + 32

	def is_below_absolute_zero(self):
		return (self.temp < -454 and self.measure == "F") or (self.temp < -270 and self.measure == "C")

tempConverterObject = TempConverter(32, "C")
print(tempConverterObject.convert())
tempConverterObject.temp = 50
print(tempConverterObject.convert())
tempConverterObject.temp = 212
print(tempConverterObject.convert())
tempConverterObject.temp = "zero"
print(tempConverterObject.convert())
tempConverterObject.temp = -500
print(tempConverterObject.convert())