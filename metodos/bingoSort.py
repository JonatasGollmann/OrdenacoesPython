# Bingo Sort é um algoritmo de ordenação que é uma variação do Selection Sort.
# Ele é eficiente para ordenar listas com muitos elementos repetidos,
# pois ele move todos os elementos iguais para a posição correta em uma única passagem.
# BIG-0 O(n * m) onde n é o número de elementos na lista e m é o número de elementos únicos.
# O(n + m^2) no melhor caso

def bingo_sort(arr):  # Ordena 'arr' in-place usando Bingo Sort e retorna métricas
    comparacoes = 0  # Contador de comparações realizadas
    trocas = 0       # Contador de trocas realizadas

    size = len(arr)  # Tamanho da lista
    if size == 0:    # Trata o caso de lista vazia
        return arr, comparacoes, trocas  # Retorna imediatamente sem ordenar

    bingo = min(arr)        # Menor valor da lista (primeiro "bingo" a ser posicionado)
    largest = max(arr)      # Maior valor da lista (limite superior usado como sentinela)
    nextBingo = largest     # Candidato ao próximo bingo (será atualizado durante a passagem)
    nextPos = 0             # Próxima posição livre onde colocar elementos iguais a 'bingo'

    while bingo < nextBingo:  # Enquanto ainda houver mais de um valor distinto a posicionar
        comparacoes += 1      # Conta a comparação do while

        startPos = nextPos    # Guarda a posição inicial desta passagem
        for i in range(startPos, size):  # Percorre os elementos ainda não posicionados
            comparacoes += 1  # Conta a comparação do if abaixo
            if arr[i] == bingo:  # Se o elemento é o bingo atual
                arr[i], arr[nextPos] = arr[nextPos], arr[i]  # Move-o para a próxima posição livre
                trocas += 1        # Contabiliza a troca
                nextPos += 1       # Avança a posição livre
            else:
                comparacoes += 1   # Conta a comparação do if interno
                if arr[i] < nextBingo:  # Se este elemento é candidato ao próximo bingo
                    nextBingo = arr[i]  # Atualiza o próximo bingo

        bingo = nextBingo       # Define o novo bingo a ser posicionado na próxima rodada
        nextBingo = largest     # Reseta o candidato ao próximo bingo para o maior valor

    return arr, comparacoes, trocas  # Retorna a lista ordenada e as métricas
