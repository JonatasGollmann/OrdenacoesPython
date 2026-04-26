# Insertion Sort
# BIG-0 O(n^2) no pior caso e O(n) no melhor caso (quando a lista já está ordenada).

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr