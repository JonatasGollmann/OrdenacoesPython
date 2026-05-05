# Bubble Sort
# BIG-0 O(n^2) no pior caso e O(n) no melhor caso (quando a lista já está ordenada).

def bubble_sort(arr):
    comparations = 0.
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
