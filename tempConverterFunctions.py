'''
Jordan Stapinski
67-495 Python Temperature Converter (structured programming solution)

Python equivalent of 67-272 lab 2: Temperature Converter

NOTE: python3 -m py_compile <THIS_FILENAME> will compile but not run the script
'''

def convert(temp, measure="F"):
	if type(temp) != int:
		return "Temperature must be an integer"
	if is_below_absolute_zero(temp, measure):
		return "Temperature below Absolute Zero"
	if (measure == "F"):
		return 5 * (temp - 32)/9
	if (measure == "C"):
		return (9 * temp)/5 + 32

def is_below_absolute_zero(temp, measure):
    return (temp < -454 and measure == "F") or (temp < -270 and measure == "C")


print(convert(32, "C"))
print(convert(50, "C"))
print(convert(212, "C"))
print(convert("zero"))
print(convert(-500, "C"))