import time

arr = [64, 34, 25, 12, 22, 11, 90]

def insertion_sort(arr):
    n = len(arr)
    for i in range(n-1):
        currentValue = arr[i]
        while i > 0 and arr[i - 1] > currentValue:
            arr[i] = arr[i -1]
            i = i - 1
        arr[i] = currentValue
        print(arr); time.sleep(1) 
        
insertion_sort(arr)