# Merge Sort
# BIG-0 O(n log n) no melhor, pior e caso médio, pois o algoritmo sempre divide a lista em duas partes e percorre cada parte uma vez.

def merge_sort(arr):  # Ponto de entrada do Merge Sort: ordena 'arr' e retorna métricas
    comparacoes = 0  # Contador de comparações entre elementos
    trocas = 0       # Contador de movimentações (gravações em 'arr')

    def merge_sort_internal(arr):  # Função recursiva interna que faz o trabalho
        nonlocal comparacoes, trocas  # Permite atualizar os contadores da função externa

        if len(arr) > 1:  # Caso recursivo: lista com mais de um elemento
            mid = len(arr) // 2  # Índice do meio
            L = arr[:mid]        # Metade esquerda
            R = arr[mid:]        # Metade direita

            merge_sort_internal(L)  # Ordena recursivamente a metade esquerda
            merge_sort_internal(R)  # Ordena recursivamente a metade direita

            i = j = k = 0  # Índices: i em L, j em R, k em arr (resultado da fusão)

            while i < len(L) and j < len(R):  # Intercala enquanto houver elementos em ambos os lados
                comparacoes += 1  # Contabiliza a comparação seguinte
                if L[i] < R[j]:   # Se o elemento da esquerda é menor
                    arr[k] = L[i]  # Coloca-o na posição k
                    i += 1         # Avança em L
                else:
                    arr[k] = R[j]  # Caso contrário, coloca o da direita
                    j += 1         # Avança em R
                trocas += 1  # Contabiliza a gravação em arr
                k += 1       # Avança a posição de gravação

            while i < len(L):  # Copia o que sobrou de L
                arr[k] = L[i]  # Grava o restante na lista final
                trocas += 1    # Contabiliza
                i += 1
                k += 1

            while j < len(R):  # Copia o que sobrou de R
                arr[k] = R[j]  # Grava o restante na lista final
                trocas += 1    # Contabiliza
                j += 1
                k += 1

    merge_sort_internal(arr)  # Inicia a recursão sobre a lista de entrada
    return arr, comparacoes, trocas  # Retorna a lista ordenada e as métricas
