// There are 6 types in javascript: number, string, boolean, object, function, undefined

// Number(prompt("Type a number", "")); // Converts string input to a number
// Boolean(prompt("Type a boolean", "")); // Converts string input to a boolean
// String(prompt("Type a string", "")); // Converts string input to a string

console.log(false == 0); // true
console.log(false === 0); // false - use triple equals if you don't want javascript to do any type conversions

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