def particao(arr, inicio, final, contadores):
    comparacoes, trocas = contadores

    pivo = arr[final]
    i = inicio - 1

    for j in range(inicio, final):
        comparacoes += 1
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            trocas += 1

    arr[i + 1], arr[final] = arr[final], arr[i + 1]
    trocas += 1

    contadores[0] = comparacoes
    contadores[1] = trocas

    return i + 1

# Quick Sort
# BIG-0 O(n log n) no melhor e caso médio, e O(n^2) no pior caso (quando a lista já está ordenada ou quase ordenada).
def quick_sort(arr, inicio=0, final=None, contadores=None):
    if contadores is None:
        contadores = [0, 0]

    if final is None:
        final = len(arr) - 1

    if inicio < final:
        pi = particao(arr, inicio, final, contadores)
        quick_sort(arr, inicio, pi - 1, contadores)
        quick_sort(arr, pi + 1, final, contadores)

    return arr, contadores[0], contadores[1]