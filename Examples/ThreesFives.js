/* Threes and Fives
Create function ThreesFives()​ that adds each value from 100 and 4000000 (inclusive)
if that value is evenly divisible by 3 or 5 but not both. Display the final sum in the console.
Second:​ Change your function to make a BetterThreesFives(start,end)​where start and end values are customizable.
 You can think of the above ThreesFives()​ function as BetterThreesFives(100,4000000)​. */ 

function ThreesFives() {
    var sum = 0; 
    for (var i=100; i<=40000; i++) {
        if ((i%3 == 0 || i%5 ==0) && (i%15 != 0)) {
            sum += i; 
        }
    }
    return sum; 
}

console.log(ThreesFives())

function BetterThreesFives(start, end) {
    var sum = 0; 
    for (var i=start; i<=end; i++) {
        if ((i%3 == 0 || i%5 ==0) && (i%15 != 0)) {
            sum += i; 
        }
    }
    return sum; 
}

console.log(BetterThreesFives(3,10))