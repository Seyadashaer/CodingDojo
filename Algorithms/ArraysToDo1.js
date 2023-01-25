    // Push Front
    function pushFront(arr, val) {
        for (let i = arr.length - 1; i >= 0; i--) {
        arr[i + 1] = arr[i];
        }
        arr[0] = val;
        return arr;
    }
    
    console.log(pushFront([5,7,2,3], 8)); // [8,5,7,2,3]
    console.log(pushFront([99], 7)); // [7,99]
    
    // Pop Front
    function popFront(arr) {
        let val = arr[0];
        for (let i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1];
        }
        arr.length--;
        console.log(arr);
        return val;
    }
    
    console.log(popFront([0,5,10,15])); // 0 returned, [5,10,15] printed
    console.log(popFront([4,5,7,9])); // 4 returned, [5,7,9] printed
    
    // Insert At
    function insertAt(arr, index, val) {
        for (let i = arr.length - 1; i >= index; i--) {
        arr[i + 1] = arr[i];
        }
        arr[index] = val;
        return arr;
    }
    
    console.log(insertAt([100,200,5], 2, 311)); // [100,200,311,5]
    console.log(insertAt([9,33,7], 1, 42)); // [9,42,33,7]
    
    // BONUS: Remove At
    function removeAt(arr, index) {
        let val = arr[index];
        for (let i = index; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1];
        }
        arr.length--;
        console.log(arr);
        return val;
    }
    
    console.log(removeAt([1000,3,204,77], 1)); // 3 returned, [1000,204,77] printed
    console.log(removeAt([8,20,55,44,98], 3)); // 44 returned, [8,20,55,98] printed
    
    // BONUS: Swap Pairs
    function swapPairs(arr) {
        for (let i = 0; i < arr.length - 1; i += 2) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
        }
        return arr;
    }
    
    console.log(swapPairs([1,2,3,4])); // [2,1,4,3]
    console.log(swapPairs(["Brendan",true,42])); // [true,"Brendan",42]
    
    // BONUS: Remove Duplicates
    function removeDuplicates(arr) {
        let j = 0;
        for (let i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[j]) {
            j++;
            arr[j] = arr[i];
        }
        }
        arr.length = j + 1;
        return arr;
    }
    
    console.log(removeDuplicates([-2,-2,3.14,5,5,10])); // [-2,3.14,5,10]
    console.log(removeDuplicates([9,19,19,19,19,19,29])); // [9,19,29]
    