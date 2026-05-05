# Bubble Sort
# BIG-0 O(n^2) no pior caso e O(n) no melhor caso (quando a lista já está ordenada).

def bubble_sort(arr):  # Ordena 'arr' in-place usando Bubble Sort
    comparations = 0.  # Contador de comparações (não utilizado no retorno)
    n = len(arr)       # Tamanho da lista
    for i in range(n):  # Faz n passagens pela lista
        for j in range(0, n-i-1):  # A cada passagem, ignora a "cauda" já ordenada
            if arr[j] > arr[j+1]:  # Se os vizinhos estão fora de ordem
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Troca os elementos
    return arr  # Retorna a lista ordenada
