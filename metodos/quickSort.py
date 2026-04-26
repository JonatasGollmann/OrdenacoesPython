def particao(arr, inicio, final):
    pivo = arr[final]
    i = inicio - 1
    for j in range(inicio, final):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[final] = arr[final], arr[i + 1]
    return i + 1

# Quick Sort
# BIG-0 O(n log n) no melhor e caso médio, e O(n^2) no pior caso (quando a lista já está ordenada ou quase ordenada).
def quick_sort(arr, inicio=0, final=None):
    if final is None:
        final = len(arr) - 1
    if inicio < final:
        pi = particao(arr, inicio, final)
        quick_sort(arr, inicio, pi - 1)
        quick_sort(arr, pi + 1, final)
    return arr
