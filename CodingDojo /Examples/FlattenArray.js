
function flattenArray(arr2d) {
    var newArray = []; 
    for (var i=0; i<arr2d.length; i++) {
        for (var j=0; j <(arr2d[i]).length; j++) {
            newArray.push(arr2d[i][j])
        }
    }
    return newArray;
}




var array1 = [ [2, 5, 8], [3, 6, 1],[5, 7, 7] ];

console.log(flattenArray(array1))