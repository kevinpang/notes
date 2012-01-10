"use strict" // This must be put at the beginning of a script or function body to enable strict mode

console.log('-------------------- Objects --------------------');
// Objects in JavaScript are simply collections of name-value pairs (similar to dictionaries in Python and hashes in Ruby).
// EVERYTHING in JavaScript is an object.
var empty_object = {}

var cat = {
    colour: "grey", 
    name: "Spot", 
    size: 46
};

console.log(cat.colour); // grey

delete cat["size"]; // // Removes the "size" property from the cat object. This could also be written as: delete cat.size
console.log(cat.size); // undefined

// Check whether a property exists on an object
console.log("size" in cat); // false
console.log("colour" in cat); // true

for(var i in cat) {
    // hasOwnProperty checks whether an object has a property defined on itself and not somewhere in its prototype chain
    if (cat.hasOwnProperty(i)) {
        console.log(i, cat[i]); // name Spot
    }
}




console.log('-------------------- Arrays --------------------');
var some_array = ["1", "2", "3"];
console.log(some_array.length); // 3
some_array[100] = "100";
console.log(some_array.length); // 101. Remember array.length isn't the # of items in the array, it's one more than the highest index

var empty_array = [];
empty_array.push("Mack");
empty_array.push("the");
empty_array.push("Knife");
console.log(empty_array.join(" ")); // "Mack the Knife"
console.log(empty_array.pop()); // "Knife"
console.log(empty_array.join(" ")); // "Mack the"




console.log('-------------------- Scope --------------------');
// Variables declared without the "var" keyword are in the global scope. Variables declared with the "var" keyword outside of any 
// functions are also in the global scope.
//
// Variables declared with the "var" keyword within a function are called local variables and are defined only within the body of 
// that function. Local variables take precedent over global variables. Local variables are also visible within any functions
// nested within the function they were defined in.

function test(o) { 
    var i = 0; // i is defined throughout function

    if (typeof o == 'object') {
        var j = 0; // j is defined everywhere, not just within the if block
        
        for (var k = 0; k < 10; k++) { // k is defined everywhere, not just within the loop
            console.log(k);
        }
        
        console.log(k); // k is still defined, will print 10
    }
    
    console.log(j); // j is defined, but may not be initialized
}

// JavaScript supports hoisting, meaning that variables declared within a function are visible even before they are declared.
// Note that initialization occurs at the location of the var statement, the value of the variable is undefined before that
// point in code. Note that function definition statements (like function "f", below) are also hoisted. However, function
// expressions that are assigned to a variable only have the variable hoisted (the variable initialization code remains where
// you placed it and is undefined until then).
var scope = 'global';

function f() {
    console.log(scope); // Prints 'undefined', not 'global'!
    var scope = 'local'; // Variable initialized here, but defined everywhere within the function
    console.log(scope); // Prints 'local'
}

// In other words, the function f could be rewritten as follows. Some JavaScript devs try to define all of their variables at
// the top of a function to make it more obvious what the true scope of their variables is:
function g() {
    var scope;
    console.log(scope);
    scope = 'local';
    console.log(scope);
}




console.log('-------------------- Closures --------------------');
// Here I have defined a function within a function. The inner function gains access to all the outer function's local variables,
// including a. The variable a is in scope for the inner function.
// 
// Normally when a function exits, all it's local variables are blown away. However, if we return the inner function and assign 
// it to a variable fnc, so that it persists after outer has exited, all of the variables that were in scope when inner was
// defined also persist. The variable a has been closed over, it is within a closure.
// 
// Note that the variable a is totally private to fnc. This is a way of creating private variables in a functional programming
// language such as JavaScript.
// 
// See http://stackoverflow.com/a/111200/1574 for a more thorough explanation
var outer = function() {
	var a = 1;

	var inner = function() {
		console.log(a);
	}

	return inner;
}

var fnc = outer();
fnc(); // 1

// Example function maker that takes advantage of closures
function makeAddFunction(amount) {
	function add(number) {
		return number + amount;
	}

	return add;
}

// This could also be written using an anonymous function:
function makeAddFunction2(amount) {
    return function (number) {
        return number + amount;
    };
}

var addTwo = makeAddFunction(2);
var addFive = makeAddFunction(5);
console.log(addTwo(1) + addFive(1)); // 3 + 6 = 9

// Here's a common mistake with using closures inside of loops. This will log the number 10 ten times since by the time the anonymous
// function has been called, the loop has already finished. Since the anonymous function closed over "i", it keeps a reference to it.
for(var i = 0; i < 10; i++) {
    setTimeout(function() {
        console.log(i);  
    }, 1000);
}

// In order to get the desired behavior (printing 0 through 9), we need to create a copy of the value i. 
for(var i = 0; i < 10; i++) {
    (function(e) {
        setTimeout(function() {
            console.log(e);  
        }, 1000);
    })(i);
}




console.log('-------------------- Module Pattern --------------------');
// Self executing anonymous function
var myNamespace = (function(){
    // Private variables / methods
    var myPrivateVar = 0;
    var myPrivateMethod = function(someText){
        console.log(someText);
    }
	
    // Public variables / methods.
    return {
        myPublicVar: "foo",	
	    myPublicFunction: function(bar){
            myPrivateVar++;
	        myPrivateMethod(bar);
	    }
    }
})();

myNamespace.myPublicVar = "blah"; // OK
myNamespace.myPublicFunction("test") // OK




console.log('-------------------- Namespacing --------------------');
// One way to namespace is to use the module pattern like above. Another way is to use an object literal (rather than a self-executing
// anonymous function which returns an object literal). You lose the benefit of private variables / methods, but it's a little easier
// to read (but you have to abide by the object literal's strict syntax).
var anotherNamespace = {
    foo: function() {
        return 'foo';
    },
    bar: function() {
        return 'bar';
    }
};

console.log(anotherNamespace.foo());
console.log(anotherNamespace.bar());




console.log('-------------------- Classes --------------------');
function Person(first, last) {
    this.first = first;
    this.last = last;
    
    // This is not the recommended way to define methods on a class (see below)
    this.fullName = function() {
        return this.first + ' ' + this.last;
    }
}

// Using the "new" keyword tells JavaScript to create a new empty object, then call the Person function with "this" set to the new
// object. Functions that are designed to be called by "new" are called constructor functions. Common practice is to capitalize the
// first letter of these functions to make it obvious that they are meant to be called by "new".
var person = new Person('Kevin', 'Pang');
console.log(person.fullName()); // Kevin Pang

// This is a better way of adding a function to the Person "class". The reason is that "fullName" has to be defined every time
// the Person constructor is called, whereas fullNameReversed is shared by all instances of Person. 
Person.prototype.fullNameReversed = function() {
    return this.last + ' ' + this.first;
}

// You can add multiple functions to the prototype using object notation like so:
Person.prototype = {
    fullNameReversed: function() {
        return this.last + ' ' + this.first;
    },
    fullNameInCaps: function() {
        return this.fullName().toUpperCase();
    }
}

var person2 = new Person('Linda', 'Ly');
console.log(person2.fullNameReversed()); // Ly Linda
console.log(person2.fullNameInCaps()); // LINDA LY




console.log('-------------------- Prototypal Inheritance --------------------');
function Shape(x, y) {
    this.x = x;
    this.y = y;
}

Shape.prototype.toString = function() {
    return 'Shape at ' + this.x + ', ' + this.y;
};

function Circle(x, y, r) {
    Shape.call(this, x, y); // invoke the base class's constructor function to take co-ords
    this.r = r;
}

Circle.prototype = new Shape();

Circle.prototype.toString = function() {
    return 'Circular ' + Shape.prototype.toString.call(this) + ' with radius ' + this.r;
}

var c = new Circle(1, 2, 3);
console.log(c.toString()); // "Circular Shape at 1, 2 with radius "3




console.log('-------------------- Misc --------------------');
// There are 6 types in javascript: number, string, boolean, object (function, array, date, regexp), null, undefined

// Expressions are evaluated to produce a value, statements are executed to make something happen (i.e.
// anything that ends with a semicolon). Expressions with side effects, such as assignment and function invocations, are expression
// statements. Similarly, var and function are declaration statements. JavaScript programs are simply a sequence of statements, 
// separated from one another with semicolons.

// Number(prompt("Type a number", "")); // Converts string input to a number
// Boolean(prompt("Type a boolean", "")); // Converts string input to a boolean
// String(prompt("Type a string", "")); // Converts string input to a string

// An important difference from other languages like Java is that in JavaScript, blocks do not have scope; only functions have scope. 
// So if a variable is defined using var in a compound statement (for example inside an if control structure), it will be visible 
// to the entire function.

console.log(false == 0); // true
console.log(false === 0); // false - use triple equals if you don't want javascript to do any type conversions

// Converts string to int. ALWAYS provide the base, otherwise it might parse values with a leading 0 in octal
console.log(parseInt('5', 10)); // 5
console.log(parseInt('11', 2)); // 3
console.log(parseInt('hello', 10)) // NaN
console.log(isNaN(parseInt('hello', 10))); // true
console.log(1 / 0); // Infinity
console.log(isFinite(1 / 0)); // false

// Conversions to number, string, boolean, and object
console.log(Number('3')); // 3, note that parseInt and parseFloat are similar, but more flexible with the input provided (e.g.
                          // they skip whitespace and parse as many numeric values as they can, even if there are alpha chars)
console.log(String(false)); // "false"
console.log(Boolean([])); // true
console.log(Object(3)); // new Number(3)

var d = new Date();
console.log(d instanceof Date); // True
console.log(d instanceof Object); // True
console.log(d instanceof Number); // False
console.log(typeof d); // object, can also be written as typeof(d)
console.log(typeof null); // object :-\, typeof only distinguishes between objects, functions, and primitive types (string, number, 
                          // boolean, undefined)

// Random idioms you might see as shorthand for convertions above
// x + "" // Same as String(x)
// +x // Same as Number(x)
// !!x // Same as Boolean(x)

// There are two ways to access properties
var text = "testing";
console.log(text.length); // 7
console.log(text["length"]); // 7
console.log(text.slice(0, 4)); // "test"

function forEach(array, action) {
	for (var i = 0; i < array.length; i++)
		action(array[i]);
}

function sum(numbers) {
	var total = 0;

	forEach(numbers, function (number) {
	    total += number;
	});

	return total;
}

console.log(sum([1, 10, 100])); // 111
console.log(Math.min(5, 6)); // 5
console.log(Math.min.apply(null, [5, 6])); // 5

function map(func, array) {
	var result = [];
	
	forEach(array, function (element) {
		result.push(func(element));
	});
  
	return result;
}

console.log(map(Math.round, [0.01, 2, 9.89, Math.PI])); // [0, 2, 10, 3]

function reduce(combine, base, array) {
	forEach(array, function (element) {
		base = combine(base, element);
	});

	return base;
}

console.log(reduce(function(a, b) {return a + b}, 0, [1, 2, 3, 4, 5])) // 15

// Any statement may be labeled by preceding it with an identifier and a colon (only useful for controlling break and continue)
var x = 0;
mainloop: while(x < 10) {
    console.log(x);
    
    if (x == 5)
        break mainloop; // This will cause this while loop to only log the numbers 0, 1, 2, 3, 4, 5
    else
        x++;
}

// Use this command to trigger a breakpoint in apps where a debugger is running (e.g. Firebug)
// debugger;