
function countPositivesInArray(arr) {
    var countPositives =0;
    for (var i=0; i<arr.length; i++) {
        if (arr[i] >0) {
            countPositives ++; 
        }
    }
    var result = "there are " + countPositives + " positive values"; 
    return result; 
}

var numbers = [3, 4, -2, 7, 16, -8, 0];
console.log(countPositivesInArray(numbers))