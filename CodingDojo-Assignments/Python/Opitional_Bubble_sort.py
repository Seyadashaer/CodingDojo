arr1 = [6,9,2,0,3,7,4,6,10,-1]

def bubbleSort(arr):
    for i in range(len(arr) -1):
        for j in range(len(arr) -1 -i):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort(arr1))