// There are 6 types in javascript: number, string, boolean, object, function, undefined

// Number(prompt("Type a number", "")); // Converts string input to a number
// Boolean(prompt("Type a boolean", "")); // Converts string input to a boolean
// String(prompt("Type a string", "")); // Converts string input to a string

console.log(false == 0); // true
console.log(false === 0); // false - use triple equals if you don't want javascript to do any type conversions

// There are two ways to access properties
var text = "testing";
console.log(text.length); // 7
console.log(text["length"]); // 7
console.log(text.slice(0, 4)); // "test"

// Objects
var cat = {colour: "grey", name: "Spot", size: 46};
console.log(cat.colour); // grey

// Removes the "size" property from the cat object
delete cat["size"]; 
console.log(cat.size); // undefined

// Arrays
var some_array = ["1", "2", "3"];
console.log(some_array.length); // 3
var empty_array = [];
empty_array.push("Mack");
empty_array.push("the");
empty_array.push("Knife");
console.log(empty_array.join(" ")); // "Mack the Knife"
console.log(empty_array.pop()); // "Knife"
console.log(empty_array.join(" ")); // "Mack the"

// Check whether a property exists on an object
console.log("size" in cat); // false
console.log("colour" in cat); // true

// Closures
outer = function() {
 var a = 1;

 var inner = function() {
   console.log(a);
 }

 return inner;
}

fnc = outer();
fnc(); // 1

// Here I have defined a function within a function. The inner
// function gains access to all the outer function's local variables,
// including a. The variable a is in scope for the inner function.
// 
// Normally when a function exits, all it's local variables are blown
// away. However, if we return the inner function and assign it to a
// variable fnc, so that it persists after outer has exited, all of the
// variables that were in scope when inner was defined also persist. The
// variable a has been closed over, it is within a closure.
// 
// Note that the variable a is totally private to fnc. This is a way
// of creating private variables in a functional programming language
// such as JavaScript.
// 
// See http://stackoverflow.com/a/111200/1574 for a more thorough explanation

// Example function maker that takes advantage of closures
function makeAddFunction(amount) {
 function add(number) {
   return number + amount;
 }
 return add;
}

// This could also be written using an anonymous function:
// function makeAddFunction(amount) {
//  return function (number) {
//    return number + amount;
//  };
// }

var addTwo = makeAddFunction(2);
var addFive = makeAddFunction(5);
console.log(addTwo(1) + addFive(1)); // 3 + 6 = 9

// To wrap your head around this, you should consider functions to not
// just package up a computation, but also an environment. Top-level
// functions simply execute in the top-level environment, that much is
// obvious. But a function defined inside another function retains access
// to the environment that existed in that function at the point when it
// was defined.
// 
// Thus, the add function in the above example, which is created when
// makeAddFunction is called, captures an environment in which amount has
// a certain value. It packages this environment, together with the
// computation return number + amount, into a value, which is then
// returned from the outer function.
// 
// When this returned function (addTwo or addFive) is called, a new
// environment---in which the variable number has a value---is created, as
// a sub-environment of the captured environment (in which amount has a
// value). These two values are then added, and the result is returned.

// Anonymous function
var add = function(a, b) {
 return a + b;
};

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

function reduce(combine, base, array) {
  forEach(array, function (element) {
    base = combine(base, element);
  });
  return base;
}

function add(a, b) {
  return a + b;
}

function sum(numbers) {
  return reduce(add, 0, numbers);
}

function map(func, array) {
  var result = [];
  forEach(array, function (element) {
    result.push(func(element));
  });
  return result;
}

console.log(map(Math.round, [0.01, 2, 9.89, Math.PI])); // [0, 2, 10, 3]

// Module pattern (self executing anonymous function)
var myNamespace = (function(){
    // Private variables / methods
    var myPrivateVar = 0;
    var myPrivateMethod = function(someText){
        console.log(someText);
    }
	
    // Public variables / methods
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

// Prototypal inheritance
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