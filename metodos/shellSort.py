# Shell Sort
# BIG-0 O(n log n) no melhor caso e O(n^2) no pior caso, dependendo da escolha dos intervalos (gaps).

def shell_sort(arr):  # Ordena 'arr' in-place usando Shell Sort e retorna métricas
    comparacoes = 0  # Contador de comparações
    trocas = 0       # Contador de deslocamentos (trocas)

    n = len(arr)  # Tamanho da lista
    gap = n // 2  # Intervalo inicial (sequência de Shell: n/2, n/4, ...)

    while gap > 0:  # Continua enquanto houver gap maior que zero
        for i in range(gap, n):  # Aplica insertion sort com o gap atual
            temp = arr[i]  # Guarda o elemento que será reinserido
            j = i  # Índice de trabalho

            while j >= gap:  # Move elementos que estão à 'gap' posições para a direita
                comparacoes += 1  # Contabiliza a comparação
                if arr[j - gap] > temp:  # Se o elemento à esquerda (gap) é maior
                    arr[j] = arr[j - gap]  # Desloca-o para a posição atual
                    trocas += 1  # Contabiliza o deslocamento
                    j -= gap  # Continua olhando 'gap' posições atrás
                else:
                    break  # Achou a posição correta — sai do laço interno

            arr[j] = temp  # Coloca o elemento guardado na posição correta

        gap //= 2  # Reduz o gap pela metade

    return arr, comparacoes, trocas  # Retorna a lista ordenada e as métricas
