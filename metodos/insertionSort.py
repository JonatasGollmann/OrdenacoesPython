# Insertion Sort
# BIG-0 O(n^2) no pior caso e O(n) no melhor caso (quando a lista já está ordenada).

def insertion_sort(arr):  # Ordena 'arr' in-place usando Insertion Sort e retorna métricas
    comparacoes = 0  # Contador de comparações
    trocas = 0       # Contador de deslocamentos (trocas)

    for i in range(1, len(arr)):  # Percorre da segunda posição até o fim
        key = arr[i]  # Elemento atual a ser inserido na parte ordenada à esquerda
        j = i - 1     # Índice do último elemento da parte já ordenada

        while j >= 0:  # Caminha para a esquerda enquanto houver elementos para comparar
            comparacoes += 1  # Contabiliza a comparação que será feita abaixo
            if key < arr[j]:  # Se a chave é menor que o elemento comparado
                arr[j + 1] = arr[j]  # Desloca o elemento uma posição à direita
                trocas += 1          # Contabiliza o deslocamento
                j -= 1               # Continua comparando com o anterior
            else:
                break  # Posição correta encontrada — sai do laço

        arr[j + 1] = key  # Insere a chave na posição correta

    return arr, comparacoes, trocas  # Retorna a lista ordenada e as métricas
