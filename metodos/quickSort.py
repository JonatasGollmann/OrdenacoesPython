def particao(arr, inicio, final, contadores):  # Particiona arr[inicio..final] em torno de um pivô
    comparacoes, trocas = contadores  # Lê os contadores atuais (passados por lista mutável)

    pivo = arr[final]  # Escolhe o último elemento como pivô
    i = inicio - 1     # Índice do final da partição "menor ou igual ao pivô"

    for j in range(inicio, final):  # Percorre os elementos da subfaixa, exceto o pivô
        comparacoes += 1  # Contabiliza a comparação
        if arr[j] <= pivo:  # Se o elemento é menor ou igual ao pivô
            i += 1  # Expande a partição da esquerda
            arr[i], arr[j] = arr[j], arr[i]  # Move o elemento para a partição correta
            trocas += 1  # Contabiliza a troca

    arr[i + 1], arr[final] = arr[final], arr[i + 1]  # Coloca o pivô em sua posição final
    trocas += 1  # Contabiliza a troca do pivô

    contadores[0] = comparacoes  # Atualiza o contador externo de comparações
    contadores[1] = trocas       # Atualiza o contador externo de trocas

    return i + 1  # Retorna a posição final do pivô

# Quick Sort
# BIG-0 O(n log n) no melhor e caso médio, e O(n^2) no pior caso (quando a lista já está ordenada ou quase ordenada).
def quick_sort(arr, inicio=0, final=None, contadores=None):  # Ordena 'arr' in-place via Quick Sort
    if contadores is None:  # Na primeira chamada não há contadores
        contadores = [0, 0]  # Inicializa [comparacoes, trocas]

    if final is None:  # Na primeira chamada também não há 'final'
        final = len(arr) - 1  # Último índice da lista

    if inicio < final:  # Caso recursivo: subfaixa com pelo menos 2 elementos
        pi = particao(arr, inicio, final, contadores)  # Particiona e obtém o índice do pivô
        quick_sort(arr, inicio, pi - 1, contadores)    # Ordena recursivamente o lado esquerdo
        quick_sort(arr, pi + 1, final, contadores)     # Ordena recursivamente o lado direito

    return arr, contadores[0], contadores[1]  # Retorna a lista ordenada e as métricas
