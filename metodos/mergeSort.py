# Merge Sort
# BIG-0 O(n log n) no melhor, pior e caso médio, pois o algoritmo sempre divide a lista em duas partes e percorre cada parte uma vez.

def merge_sort(arr):
    comparacoes = 0
    trocas = 0

    def merge_sort_internal(arr):
        nonlocal comparacoes, trocas

        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            merge_sort_internal(L)
            merge_sort_internal(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                comparacoes += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                trocas += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                trocas += 1
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                trocas += 1
                j += 1
                k += 1

    merge_sort_internal(arr)
    return arr, comparacoes, trocas