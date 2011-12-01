from sys import argv

print "Hello World!"

print """
Use triple quotes to 
do multi-line strings
"""

# Functions
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
print_two("Kevin", "Pang")
print_two_again("Kevin", "Pang")

# Logic operators: and, or, not, !=, ==, >=, <=
print not True # False
print True == False # False

# If / else
var_1 = 1
var_2 = 2

if var_1 > var_2:
	print "1 > 2"
elif var_1 == var_2:
	print "1 = 2"
else:
	print "1 < 2"
	
# Lists
print "--- Lists --- "
colors = ["red", "white", "blue"]
colors.append("green")

print range(0, 5) # [0, 1, 2, 3, 4]
print range(0, 5, 2) # [0, 2, 4]
print colors[0] # red
print colors[-1] # green

# For loops
print "--- For loops ---"
for color in colors:
	print color

for i in range(0, len(colors)):
	print colors[i]

# While loops
print "--- While loops ---"
i = 0
while i < len(colors):
	print colors[i]
	i += 1

# Dictionaries / Hashes
print "--- Dictionaries / Hashes ---"
stuff = {"name" : "Kevin", "age" : 29}
print stuff["name"]
print stuff["age"]
print stuff # {'age':29, 'name':'Kevin'}
del stuff["age"]
print stuff # {'name':'Kevin'}
print "age" in stuff # False
print "name" in stuff # True

# Classes
print "--- Classes ---"
class Car(object):
	def __init__(self):
		self.miles = 0
		
	def drive(self, miles):
		self.miles += miles
		
	def print_mileage(self):
		print self.miles

car = Car()
car.drive(50)
car.print_mileage()

# Inheritance
class Hummer(Car):
	def drive(self, miles):
		self.miles += 2 * miles
		
hummer = Hummer()
hummer.drive(50)
hummer.print_mileage()

# IO
if False:
	# Get input from command line
	age = raw_input("How old are you? ")
	print "You are %s years old!" % age

	# Parses command line arguments
	script, user_name = argv
	print "Hello %s, I am the %s script" % (user_name, script)
	
	# Read files (r for reading, w for writing)
	txt = open("python_notes.py", "r")
	print txt.read()
	txt.close()