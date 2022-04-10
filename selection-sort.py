import time

arr = [64, 34, 25, 12, 22, 11, 90]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n-1):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr); time.sleep(1) 

selection_sort(arr)
