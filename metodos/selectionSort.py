# Selection Sort
# BIG-0 O(n^2) no pior caso e O(n^2) no melhor caso, pois ele sempre percorre toda a lista para encontrar o menor elemento.

def selection_sort(arr):  # Ordena 'arr' in-place usando Selection Sort e retorna métricas
    comparacoes = 0  # Contador de comparações
    trocas = 0       # Contador de trocas

    n = len(arr)  # Tamanho da lista
    for i in range(n):  # Para cada posição da lista
        min_idx = i  # Assume inicialmente que o menor está em 'i'
        for j in range(i + 1, n):  # Procura o menor entre os elementos restantes
            comparacoes += 1  # Contabiliza a comparação
            if arr[j] < arr[min_idx]:  # Se encontrou um elemento menor
                min_idx = j  # Atualiza o índice do mínimo

        if min_idx != i:  # Se o mínimo não estava em 'i', precisa trocar
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Coloca o menor na posição 'i'
            trocas += 1  # Contabiliza a troca

    return arr, comparacoes, trocas  # Retorna a lista ordenada e as métricas
