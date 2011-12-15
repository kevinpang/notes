from sys import argv
from functools import partial

# Alternative way of writing the above, but any calls to argv would need to be fully qualified (i.e. sys.argv)
# import sys.argv

# Misc
# Logic operators: and, or, not, !=, ==, >=, <=

print isinstance(None, object) # True (None is Python's version of null)
print issubclass(str, object) # True
print None is None # True (There is only one None)
print type(1) # <type 'int'>
print None.__class__ # <type 'NoneType'>
# print dir(sys) # Displays names defined in module 'sys'
# print dir() # Displays named defined currently
# print dir(__builtin__) # Displays names of built-in functions and variables

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

print """
Use triple quotes to 
do multi-line strings
"""

hello_world = 'Hello' ', ' 'world'
print hello_world # 'Hello, world'

# String interpolation
print 'String interpolation {0} {1}'.format('Hello', 'world') # Hello world'
print 'String interpolation {foo} {bar}'.format(foo = 'Hello', bar = 'world') # Hello world!
print 'String interpolation %s %s' % ('Hello', 'world') # Hello world! <-- old style (deprecated)

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
	print 'arg1: %r, arg2: %r'.format(arg1, arg2)
	
def print_two_again(arg1, arg2):
	print 'arg1: %r, arg2: %r'.format(arg1, arg2)
	
print_two('Kevin', 'Pang')
print_two_again('Kevin', 'Pang')
print print_two.__doc__ # 'A string placed at the beginning of a function is used as documentation'

# Functions are objects too, so you can assign them to variables
test = print_two
test('Kevin', 'Pang')

# Simulating Ruby's "each" method. Not as elegant without blocks since you have to define the function elsewhere (or use a lambda),
# but at least it's doable. It would probably be more Pythonic to simply do something like:
#
# for item in my_list:
# 	add_s(item)
class MyList(list):
	def each(self, func):
		for item in self:
			func(item)

def add_s(item):
	print item + 's'
			
my_list = MyList()
my_list.append('banana')
my_list.append('grape')
my_list.each(add_s)

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
	total_cars = 0 # Class variable (any variables defined outside of a function are class variables)
	
	def __init__(self):
		self.miles = 0
		self.make = ''
		Car.total_cars += 1
		
	def drive(self, miles):
		self.miles += miles
		
	def print_mileage(self):
		print self.miles
		
	def _pseudo_private_method(self):
		# Prefixing a method with an underscore implies private scope (but not enforced, there are no private methods / variables
		# in Python)
		print 'pseudo private method'
		
	def __more_private_method(self):
		# Prefixing a method with double underscore makes it harder to use directly due to name mangling, but you can still access it
		print 'more private method'
	
	# Creating properties via decorators	
	@property
	def make(self):
		return self._make
		
	@make.setter
	def make(self, a_make):
		self._make = a_make
		
	def __str__(self):
		return self._make
		
	def __repr__(self):
		return self._make + ' ' + str(self.miles)
		
car = Car()
car.drive(50)
car.print_mileage()
car._pseudo_private_method() # This works!
car._Car__more_private_method() # This works too! Nothing is private!
car.make = 'Honda'
print car.make # Honda
print str(car) # Honea
print repr(car) # Honda 50

# Inheritance
class Hummer(Car):
	def drive(self, miles):
		self.miles += 2 * miles
		
	def print_mileage(self):
		super(Hummer, self).print_mileage() # This is how you invoke the parent class
		
hummer = Hummer()
hummer.drive(50)
hummer.print_mileage()

print Car.total_cars # 2

# Monkey patching
print '--- Monkey patching ---'
class Dog(object):
	def bark(self):
		return 'WOOF'
		
def wag(self):
	return 'HAPPY'
	
Dog.wag = wag

a_dog = Dog()
print a_dog.bark() # WOOF
print a_dog.wag() # HAPPY

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

# Map transforms elements of a list
print '--- Map ---'
def add_ten(item):
	return item + 10

seq = [1, 2, 3]
mapped_seq = map(add_ten, seq) 

print seq # [1, 2, 3]
print mapped_seq # [11, 12, 13]

# Reduce applies a function to each item of the list and accumulates the values to reduce the list to a single value
print '--- Reduce ---'
def add(accumulated_value, item):
	return accumulated_value + item

def multiply(accumulated_value, item):
	return accumulated_value * item	

print reduce(add, [1, 2, 3]) # 1 + 2 + 3 = 6
print reduce(multiply, [1, 2, 3], 1) # 1 * 1 * 2 * 3 = 6

# List comprehensions
print '--- List comprehensions ---'
meats = ['ham', 'turkey', 'steak']
print [meat.upper() for meat in meats] # ['HAM', 'TURKEY', 'STEAK']
print map(lambda meat: meat.upper(), meats) # This is equivalent to the above

def upper_meat(meat):
	return meat.upper()
	
print map(upper_meat, meats) # This is also equivalent

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
	
# Iterators
print '--- Iterators ---'
it = iter(range(0, 6))

for num in it:
	print num # 0 1 2 3 4 5

it = iter(range(0, 6))
print next(it) # 0
print next(it) # 1

# Enums
print '--- Enums ---'

# Python doesn't have support for Enums, but you can make your own via classes
class Colors:
	RED = 1
	BLUE = 2
	GREEN = 3
	
print Colors.RED # 1
# print Colors.ORANGE # This will throw an AttributeError exception since Colors doesn't contain an attribute called ORANGE 

# This is useful when writing Python scripts that need to be usable as both scripts run from the command line
# as well as modules imported from other Python modules.
if __name__ == "__main__":
	print 'This script was run from the command line'

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
	
	# Reading files using the with statement
	with open('python_notes.py', 'r') as f:
		print f.read()
	
# Packages
# Putting an __init__.py file into a directory makes Python treat the directory as containing packages. It can
# be empty or you can p initialization code for the package in there. Some package authors will define an
# __all__ list inside __init__.py so that anyone importing * from the package will get all the names listed
# within the package's __all__ list (this is by convention).

# Decorating with functions
print '--- Decorating with functions ---'
def addCowbell(fn):
	fn.foo = 'foo'
	return fn

@addCowbell
def bar():
	return 'bar'
	
print bar.foo # foo

# Partials
print '--- Partials ---'
def max(a, b):
	if a > b:
		return a
	else:
		return b
		
max100 = partial(max, 100)

print max100(50) # 100
print max100(150) # 150

# Decorators
print '--- Decorators ---'

# Decorators are wrappers that let you execute code before and after the function they decorate
def makebold(fn):
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def makeitalic(fn):
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

# say = makebold(makeitalic(say)) # This is equivalent to using the decorators above

print say() # <b><i>hello</i></b>

# Metaclasses (note that these aren't very frequently used!)
print '--- Metaclasses ---'

def some_method(self):
	print 'some_method'

# You can dynamically create classes by using the "type" function. The 2nd argument is a tuple of the parent class(es). 
# The 3rd argument is a dictionary containing attribute names and values
MyOtherShinyClass = type('MyOtherShinyClass', (), {'some_attribute' : True, 'some_method' : some_method}) 
													  
print MyOtherShinyClass # <class '__main__.MyOtherShinyClass'>
print MyOtherShinyClass.some_attribute # True

an_instance = MyOtherShinyClass()
an_instance.some_method() # some_method

# Metaclasses are classes that create classes (i.e. a class factory). When Python sees a class definition, it checks if
# the class definition contains a __metaclass__ attribute. If so, it will use it to create the class object. If not, it
# will go to the parent class and try to do the same thing. If it can't find any __metaclass__ attributes, it falls back to
# using the "type" function to create the class object.
#
# The main purpose of using metaclasses is to change the class automatically, when it's created.

# Using a function as a metaclasses
def upper_attr(future_class_name, future_class_parents, future_class_attr):
	"""
	  Return a class object, with the list of its attribute turned 
	  into uppercase.
	"""

  	# pick up any attribute that doesn't start with '__'
	attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
	# turn them into uppercase
	uppercase_attr = dict((name.upper(), value) for name, value in attrs)

	# let `type` do the class creation
	return type(future_class_name, future_class_parents, uppercase_attr)

class Foo(object):
	__metaclass__ = upper_attr
	 
	# we can define __metaclass__ here instead to affect only this class
	bar = 'bip'

f = Foo()
print hasattr(Foo, 'bar') # False
print hasattr(Foo, 'BAR') # True
print f.BAR # bip

# Using a class as a metaclass
class UpperAttrMetaclass(type): 
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
    def __new__(self, future_class_name, future_class_parents, future_class_attr):
		attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
		uppercase_attr = dict((name.upper(), value) for name, value in attrs)

		# return type(future_class_name, future_class_parents, uppercase_attr) # Same as below, but less OOP
		return type.__new__(self, future_class_name, future_class_parents, uppercase_attr)
		# return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr) # Yet another way, in case this metaclass inherits from another metaclass
		
class Foo2(object):
	__metaclass__ = UpperAttrMetaclass
	
	bar = 'bip'
	
f2 = Foo2()
print hasattr(Foo2, 'bar') # False
print hasattr(Foo2, 'BAR') # True
print f2.BAR # bip