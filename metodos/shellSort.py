# Shell Sort
# BIG-0 O(n log n) no melhor caso e O(n^2) no pior caso, dependendo da escolha dos intervalos (gaps).

def shell_sort(arr):
    comparacoes = 0
    trocas = 0

    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap:
                comparacoes += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    trocas += 1
                    j -= gap
                else:
                    break

            arr[j] = temp

        gap //= 2

    return arr, comparacoes, trocas