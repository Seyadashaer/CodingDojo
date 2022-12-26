function isPalindrome(arr) {
    var leftIndex = 0; 
    var rightIndex = arr.length -1; 
    while (leftIndex < rightIndex) { 
        if (arr[leftIndex] != arr[rightIndex]) {
            return "Not Palindrome!"
        } 
        leftIndex ++;
        rightIndex --; 
    }
    return "Palindrome"
}

var result1 = isPalindrome( [1, 1, 2, 3, 1] );
console.log(result1);