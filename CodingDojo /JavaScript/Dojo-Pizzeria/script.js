function pizzaOven(crustType, sauceType, cheeses, toppings) {
    var pizza = {}; 
    pizza.crustType = crustType;
    pizza.sauceType = sauceType;
    pizza.cheeses = cheeses;
    pizza.toppings = toppings;
    return pizza; 
}
var firstPizza = pizzaOven("deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"]);
var secondPizza = pizzaOven("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);
var thirdPizza = pizzaOven("deep dish", "marinara", ["mozzarella"],  ["sausage", "tomatos"]);
var fourthPizza = pizzaOven("hand tossed", "traditional", ["feta"],  ["olives", "onions"]);

function randomPizza() { 
    
}