from sys import argv

print 'Hello World!'

print """
Use triple quotes to 
do multi-line strings
"""

# Logic operators: and, or, not, !=, ==, >=, <=

# Misc
print isinstance(None, object) # True (None is Python's version of null)
print issubclass(str, object) # True
print None is None # True (There is only one None)
print type(1) # <type 'int'>
print None.__class__ # <type 'NoneType'>

class Parent(object): pass
class Child(Parent): pass

# __mro__ (can also use the mro() function) is the Method Resolution Order. It returns a tuple listing the types
# the class is derived from, in the order they are searched for methods.
print Child.__mro__ # (<class '__main__.Child'>, <class '__main__.Parent'>, <type 'object'>)
print Child.__mro__.__class__ # <type 'tuple'>
print Child.__mro__.__class__.__name__ # tuple

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

print sorted([5, 4, 3, 2, 1]) # [1, 2, 3, 4, 5]
another_list = [5, 4, 3, 2, 1]
another_list.sort()
print another_list # [1, 2, 3, 4, 5]

# Filter selects certain items from a list
def is_even(item):
	return item % 2 == 0

seq = [1, 2, 3, 4, 5, 6]
filtered_seq = filter(is_even, seq)

print seq # [1, 2, 3, 4, 5, 6]
print filtered_seq # [2, 4, 6]

# Map transforms elements of a list
def add_ten(item):
	return item + 10

seq = [1, 2, 3]
mapped_seq = map(add_ten, seq) 

print seq # [1, 2, 3]
print mapped_seq # [11, 12, 13]

# Reduce applies a function to each item of the list and accumulates the values to reduce the list to a single value
def add(accumulated_value, item):
	return accumulated_value + item

def multiply(accumulated_value, item):
	return accumulated_value * item	

print reduce(add, [1, 2, 3]) # 1 + 2 + 3 = 6
print reduce(multiply, [1, 2, 3], 1) # 1 * 1 * 2 * 3 = 6

# List comprehensions
meats = ['ham', 'turkey', 'steak']
print [meat.upper() for meat in meats] # ['HAM', 'TURKEY', 'STEAK']

# Generators (slightly different than list comprehensions b/c generators must be iterated through, the values are 
# generated on the fly rather than stored. Generators are memory friendly, but less versatile.)
print '--- Generators ---'
result = []
bacon_generator = (n + ' bacon' for n in ['crunchy', 'veggie', 'danish'])
for bacon in bacon_generator:
	result.append(bacon)
	
print result # ['crunchy bacon', 'veggie bacon', 'danish bacon']

dynamite = ('Boom!' for n in range(3))

attempt_1 = list(dynamite) # ['Boom!', 'Boom!', 'Boom!]
attempt_2 = list(dynamite) # [] <-- This is because generators are a one shot deal

print list(attempt_1)
print list(attempt_2)

# The presence of the yield keyword turns abc into a generator factory. Execution starts when the next() routine is invoked, then
# stops when the first yield keyword is hit. Then resumes when next() is invoked again, then stops wen the next yield keyword is hit.
def abc():
	yield "a"
	yield "b"
	yield "c"
	
generator_factory = abc()
print generator_factory.next() # a
print generator_factory.next() # b
print generator_factory.next() # c

def simple_generator_method():
	yield 'peanut'
	yield 'butter'
	yield 'and'
	yield 'jelly'
	
result = []

for item in simple_generator_method(): # The for loop will invoke the next() routine on simple_generator_method
	result.append(item)
	
print result # ['peanut', 'butter', 'and', 'jelly']

def square_me(seq):
	for x in seq:
		yield x * x
	
square_me_generator = square_me(range(5))

for item in square_me_generator:
	print item # 0, 1, 4, 9, 16

# This will also work, since converting to a list will iterate via the next() routine
# print list(square_me_generator) # [0, 1, 4, 9 ,16]

def fibon(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

for x in fibon(5):
	print x # 1 1 2 3 5

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
finally:
	print "Finally!"
	
try:
	raise Exception("1", "2")
except Exception as ex:
	print ex.args[0] # 1
	print ex.args[1] # 2
	
	var_1, var_2 = ex
	
	print var_1 # 1
	print var_2 # 2
	
try:
	pass
except Exception as ex:
	print 'This shouldn\'t be hit!'
else:
	print "Yay!" # Yay!

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
	
def make_incrementor_without_lambdas(n):
	# This is equivalent to using a lambda, except you can define multi-line functions
	def foo(x):
		return x + n
		
	return foo
	
f = make_incrementor(42)
print f(0) # 42
print f(1) # 43

f = make_incrementor_without_lambdas(42)
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

# Iterators
print '--- Iterators ---'
it = iter(range(0, 6))

for num in it:
	print num # 0 1 2 3 4 5
	
it = iter(range(0, 6))
print next(it) # 0
print next(it) # 1

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