function d6() {
    var roll = Math.floor(Math.random() * (6-1) + 1) ;
    return roll;
}
var playerRoll = d6();
console.log("The player rolled: " + playerRoll);





function getRandom(min, max) {
    return(Math.floor(Math.random() * (max -min ) + min));
}
console.log(getRandom(1,6))