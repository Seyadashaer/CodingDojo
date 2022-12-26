
function reverseArray(arr) { 
    var leftIndex = 0;
    var rightIndex = arr.length -1;

    while (leftIndex < rightIndex) { 
        var temp = arr[leftIndex]; 
        arr[leftIndex] = arr[rightIndex]; 
        arr[rightIndex] = temp; 

        leftIndex ++; 
        rightIndex --;
    }
    return arr; 

}

var result1 = reverseArray([1,6,8,9,3,6,5,0])
console.log(result1)