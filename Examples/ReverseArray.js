function reverseArray(arr) {
    var left = 0; 
    var right = arr.length -1; 
    while(left < right) {
        var temp = arr[left];
        arr[left] = arr[right]
        arr[right] = temp; 
    }
    return arr;
}

console.log(reverseArray([1,6,9,3,5,7]))