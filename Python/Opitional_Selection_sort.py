arr1 = [6,9,2,0,3,7,4,6,10,-1]

def selectionSort(arr):
    for i in range(len(arr) -1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selectionSort(arr1))



