/*Factorial
Write a function factorial(num)​ that, given a number, 
returns the product (multiplication) of all positive integers from 1 up to number (inclusive).
 For example, factorial(3)​ = 6 (or 1 * 2 * 3); factorial(5)​ = 120 (or 1 * 2 * 3 * 4 * 5) */ 

function factorialNumber(num) {
    var result = 1; 
    for (var i=1; i<=num; i++){
        result *= i; 
    }
    return result; 
}



console.log(factorialNumber(5));
console.log(factorialNumber(1));
console.log(factorialNumber(3));
console.log(factorialNumber(0))



