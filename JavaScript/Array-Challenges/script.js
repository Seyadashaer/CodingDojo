// 1. Always Hungry
function alwaysHungry(arr) {
    var foodCount = 0;
    for(var i=0; i<arr.length; i++) {
        if (arr[i] =="food") {
            console.log("Yummy");
            foodCount ++;
        }
    }
    if (foodCount == 0) {
        console.log("I'm Hungry!");
    }
}

// 2. High Pass Filter
function highPass(arr, cutoff) {
    var filteredArr = [];
    for (var i=0; i<arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

// 3. Better than average
function betterThanAverage(arr) {
    var sum = 0;
    for (var i=0; i<arr.length; i++) {
        sum += arr[i]
        var average = sum/arr.length;
    }
    var count = 0;
    for (var i=0; i<arr.length; i++) {
        if (arr[i] > average) {
            count++;
        }
    }
    return count;
}

// 4. Array Reverse

function reverse(arr) { 
    var left = 0; 
    var right = arr.length -1; 
    while (left < right) { 
        var temp = arr[left];
        arr[left] = arr[right]; 
        arr[right] = temp; 
        left ++; 
        right --; 
    }
    return arr; 
}

// 5. Fibonacci Array
function fibonacciArray(n) {
    var fibArr = [0, 1];
    while(fibArr.length < n) {
        var lastElement = fibArr[fibArr.length -1];
        var beforeLastElement = fibArr[fibArr.length -2];
        var newElement = lastElement + beforeLastElement;
        fibArr.push(newElement); 
    }
    return fibArr;
}


