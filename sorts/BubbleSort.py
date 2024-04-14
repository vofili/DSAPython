def doBubbleSort(arr):
    for i in range(len(arr) - 1,0,-1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

testArr = [23,4,19,5,88,12]
doBubbleSort(testArr)
print(testArr)