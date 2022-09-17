"""
CELSIUS - FAHRENHEIT CONVERTER

formulas:
c * 9/5 + 32 = f
(f - 32) * 5/9 = c
"""

from sys import exit

def error (n):
	print '"%s" is not a number.\n' % string


def f2c(f):
	try:
		f = int(f)
		c = (f - 32) * 5/9
		print "%d degrees fahrenheit are %d degrees celsius\n" % (f, c)
	except ValueError:
		error(f)

def c2f(c):
	try:
		c = int(c)
		f = c * 9/5 + 32
		print "%d degrees celsius are %d degrees fahrenheit\n" % (c, f)
	except ValueError:
		error(c)

def choice(x):
	try:
		x = int(x)
		if x == 1:
			degrees = raw_input("Please enter degrees to be converted: ")
			c2f(degrees)
		elif x ==2:
			degrees = raw_input("Please enter degrees to be converted: ")
			f2c(degrees)
		elif x ==3:
			print "Thank you for using this App!"
			exit(1)
		else:
			print '"%d" is not 1, 2 or 3.\n' % x
	except ValueError:
		error(x)




intro = '''CELSIUS - FAHRENHEIT CONVERTER
Made in Python by Giannis Terzakis
------------------------------------
'''

ctext = '''Please select one of the following:
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
3. Quit the converter
'''

print intro

while 1:
	print ctext
	choice(raw_input("Choice: "))