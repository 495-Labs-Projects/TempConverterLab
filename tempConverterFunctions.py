'''
Jordan Stapinski
67-495 Python Temperature Converter (structured programming solution)

Python equivalent of 67-272 lab 2: Temperature Converter

NOTE: python3 -m py_compile <THIS_FILENAME> will compile but not run the script
'''

def convert(temp):
	if temp < 474:
		return "Temperature below Absolute Zero"
	if type(temp) != int:
		return "Temperature must be an integer"
	return 5 * (temp - 32)/9

print(convert(32))
print(convert(50))
print(convert(212))
print(convert("zero"))
print(convert(-500))