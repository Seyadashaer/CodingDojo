// Reverse Array

function reverseArray(arr) {
    let start = 0;
    let end = arr.length - 1;
    while (start < end) {
        let temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
    return arr;
}
  console.log(reverseArray([1,2,3,4,5]));  // [5,4,3,2,1]
  console.log(reverseArray([100,200,300])); // [300,200,100]


// Rotate Array

function rotateArray(arr, shiftBy) {
    shiftBy = shiftBy % arr.length;
    if (shiftBy < 0) {
        shiftBy = shiftBy + arr.length;
    }

    let reverse = (arr, start, end) => {
        while (start < end) {
            let temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    reverse(arr, 0, arr.length - 1);
    reverse(arr, 0, shiftBy - 1);
    reverse(arr, shiftBy, arr.length - 1);
    return arr;
}
console.log(rotateArray([1, 2, 3, 4, 5], 1));  // [5,1,2,3,4]
console.log(rotateArray([1, 2, 3, 4, 5], -1));  // [2,3,4,5,1]
console.log(rotateArray([1, 2, 3, 4, 5], 2)); // [4,5,1,2,3]


// Filter Range 

function filterRange(arr, min, max) {
    let j = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] >= min && arr[i] <= max) {
            arr[j++] = arr[i];
        }
    }
    arr.length = j;
    return arr;
}
console.log(filterRange([1,2,3,4,5,6,7,8],3,6)); // [3,4,5,6]
console.log(filterRange([-5,10,0,15,20],-1,5));  // [-5,0]


//Array Concat

function arrayConcat(arr1,arr2){
    let newArr = arr1.slice();
    for (let i = 0; i < arr2.length; i++) {
        newArr.push(arr2[i]);
    }
    return newArr;
}
console.log(arrayConcat(['a','b'], [1,2]));  // ['a','b',1,2]
console.log(arrayConcat([1,2,3], [4,5,6])); // [1,2,3,4,5,6]
