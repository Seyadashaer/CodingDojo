/* Generate Coin Change
Implement generateCoinChange(cents)​ that accepts a parameter for the number of cents,
and computes how to represent that amount with the smallest number of coins. Console.log the result. 
A penny is worth 1 cent. A nickel is worth 5 cents. A dime is worth 10 cents. A quarter is worth 25 cents.*/ 


function generateCoinChange(cents) {
    var coinChange = []; 
    var quarters = 0; 
    var dimes = 0; 
    var nickels = 0; 
    var pennies = 0; 
    while(cents > 0) {
        if (cents>25) {
            cents -= 25; 
            quarters ++;
        } else if (cents>10) {
            cents -= 10; 
            dimes ++; 
        } else if (cents > 5 ) {
            cents -=5;
            nickels ++;
        } else if (cents>=1) {
            cents -= 1; 
            pennies ++; 
        }
    }
    coinChange.push("quarters: "  + quarters);
    coinChange.push("dimes: " + dimes);
    coinChange.push("nickels: " + nickels);
    coinChange.push("pennies: " + pennies);
    return coinChange;
    }

console.log(generateCoinChange(167));




