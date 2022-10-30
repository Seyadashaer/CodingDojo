function isPalindrome(arr) {
    var left = 0; 
    var right = arr.length -1 
    while(left < right) {
        if (arr[left] != arr[right]) {
            return "Not a Palindrome";
        }
        left ++;
        right --; 
    }
    return "Palindrome";
}

var result1 = isPalindrome( [1, 1, 2, 1, 1] );
console.log(result1);