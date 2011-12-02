from sys import argv

print 'Hello World!'

print """
Use triple quotes to 
do multi-line strings
"""

# Logic operators: and, or, not, !=, ==, >=, <=

# Misc
print isinstance(None, object) # True (None is Python's version of null)
print None is None # True (There is only one None)
print type(1) # <type 'int'>
print None.__class__ # <type 'NoneType'>

# Strings
print '--- Strings ---'
print 'This is a \n test' # Test will appear on a new line
print r'This is a \n test' # Raw string, backslash doesn't act as an escape character
print 'It was the best of times. \
It was the worst of times.' # Use backslash to continue string on next line 'It was the best of times. It was the worst of times.'

hello_world = 'Hello' ', ' 'world'
print hello_world # 'Hello, world'

print 'String interpolation {0} {1}'.format('Hello', 'world') # 'String interpolation Hello world'
print 'String interpolation %s %s' % ('Hello', 'world') # 'String interpolation Hello world'

words = ['Now', 'is', 'the', 'time']
print ' '.join(words) # 'Now is the time'

print 'foo'.capitalize() # 'Foo'
print 'foo'.upper() # 'FOO'
print 'FOO'.lower() # 'foo'
print 'kevin william pang'.title() # 'Kevin William Pang'
print 'A b C'.swapcase() # 'a B c'

# Functions
print '--- Functions ---'
def print_two(*args):
	'A string placed at the beginning of a function is used as documentation'
	arg1, arg2 = args
	print 'arg1: %r, arg2: %r' % (arg1, arg2)
	
def print_two_again(arg1, arg2):
	print 'arg1: %r, arg2: %r' % (arg1, arg2)
	
print_two('Kevin', 'Pang')
print_two_again('Kevin', 'Pang')
print print_two.__doc__ # 'A string placed at the beginning of a function is used as documentation'

# Functions are objects too, so you can assign them to variables
test = print_two
test('Kevin', 'Pang')

def empty_method(self):
	pass
	
def one_line_method(self): return 'foo'

def pass_in_list_and_dictionary(*arr, **dict):
	for arr_item in arr:
		print arr_item

	for key in dict.keys():
		print key, ':', dict[key]

pass_in_list_and_dictionary(1, 2, 3, a=4, b=5, c=6) # 1, 2, 3, a:4, b:5, c:6

# If / else
var_1 = 1
var_2 = 2

if var_1 > var_2:
	print '1 > 2'
elif var_1 == var_2:
	print '1 = 2'
else:
	print '1 < 2'
	
# Lists
print '--- Lists --- '
colors = ['red', 'blue']
colors.append('green')
colors.insert(1, 'white')
colors.append('gold')
colors.pop()
print colors # ['red', 'white', 'blue', 'green']

print range(0, 5) # [0, 1, 2, 3, 4]
print range(0, 5, 2) # [0, 2, 4]
print colors[0] # red
print colors[-1] # green

# Slice notation
print colors[2:4] # ['blue', 'green']
print colors[:2] # From beginning to index 2 ['red', 'white']
print colors[2:] # From index 2 to end ['blue', 'green']

empty_list = list()
print len(empty_list) # 0

another_empty_list = []
print len(another_empty_list) # 0

empty_list[0:] = [1, 2, 3] 
print empty_list # [1, 2, 3]

# Sets
print '--- Sets ---'
highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']
there_can_be_only_one = set(highlanders)
print len(highlanders) # 7
print len(there_can_be_only_one) # 4

print set('12345') # set(['1', '2', '3', '4', '5'])

# Tuples
print '--- Tuples ---'
a_tuple = (1, 2, 3) # Immutable, cannot assign new values or append
print a_tuple[1] # 2
a_list = list(a_tuple) # Convert tuple to list
a_list.append(4)
print a_list # [1, 2, 3, 4]
a_tuple = tuple(a_list)
print a_tuple # (1, 2, 3, 4)

empty_tuple = ()
another_empty_tuple = tuple()

# For loops
print '--- For loops ---'
for color in colors:
	print color

for i in range(0, len(colors)):
	print colors[i]

# While loops
print '--- While loops ---'
i = 0
while i < len(colors):
	print colors[i]
	i += 1

# Dictionaries / Hashes
print '--- Dictionaries / Hashes ---'
stuff = {'name' : 'Kevin', 'age' : 29}
print stuff['name']
print stuff['age']
print stuff # {'age':29, 'name':'Kevin'}
print stuff.keys() # ['age', 'name']
print stuff.values() # [29, 'Kevin']
del stuff['age']
print stuff # {'name':'Kevin'}
print 'age' in stuff # False
print 'name' in stuff # True

empty_dictionary = dict()
print len(empty_dictionary) # 0
another_empty_dictionary = {}
print len(another_empty_dictionary) # 0

# Try / Catch
print '--- Try / Catch ---'
try:
	None.some_method_none_does_not_know_about()
except Exception as ex:
	print ex.__class__.__name__ # AttributeError
	print ex.args[0] # 'NoneType' object has no attribute 'some_method_none_does_not_know_about'

# Classes
print '--- Classes ---'
class Car(object):
	def __init__(self):
		self.miles = 0
		
	def drive(self, miles):
		self.miles += miles
		
	def print_mileage(self):
		print self.miles
		
	def _private_method(self):
		# Prefixing a method with an underscore implies private scope (but not enforced)
		pass
		
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

# Lambdas
print '--- Lambdas ---'
def make_incrementor(n):
	return lambda x: x + n # Creates an anonymous function, restricted to a single expression
	
f = make_incrementor(42)
print f(0) # 42
print f(1) # 43

# Enums
print '--- Enums ---'

# Python doesn't have support for Enums, but you can make your own via classes
class Colors:
	RED = 1
	BLUE = 2
	GREEN = 3
	
print Colors.RED # 1
# print Colors.ORANGE # This will throw an AttributeError exception since Colors doesn't contain an attribute called ORANGE 

# IO
if False:
	# Get input from command line
	age = raw_input('How old are you? ')
	print 'You are %s years old!' % age

	# Parses command line arguments
	script, user_name = argv
	print 'Hello %s, I am the %s script' % (user_name, script)
	
	# Read files (r for reading, w for writing)
	txt = open('python_notes.py', 'r')
	print txt.read()
	txt.close()