


function isPresent2d(arr2d, value) { 
    for (var i=0; i<arr2d.length; i++) {
        for (var j=0; j<arr2d[i].length; j++) {
            if (arr2d[i][j] === value){
                return true;
            }
        }
    }
    return false;
}

var array1 = [ [2, 5, 8], [3, 6, 1],[5, 7, 7] ];
    

result1 = isPresent2d(array1, 90);
console.log(result1)