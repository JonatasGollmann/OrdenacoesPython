# Bingo Sort é um algoritmo de ordenação que é uma variação do Selection Sort. 
# Ele é eficiente para ordenar listas com muitos elementos repetidos, 
# pois ele move todos os elementos iguais para a posição correta em uma única passagem.
# BIG-0 O(n * m) onde n é o número de elementos na lista e m é o número de elementos únicos.
# O(n + m^2) no melhor caso

def bingo_sort(arr):
    comparacoes = 0
    trocas = 0

    size = len(arr)
    if size == 0:
        return arr, comparacoes, trocas
    
    bingo = min(arr)
    largest = max(arr)
    nextBingo = largest
    nextPos = 0

    while bingo < nextBingo:
        comparacoes += 1

        startPos = nextPos
        for i in range(startPos, size):
            comparacoes += 1
            if arr[i] == bingo:
                arr[i], arr[nextPos] = arr[nextPos], arr[i]
                trocas += 1
                nextPos += 1
            else:
                comparacoes += 1
                if arr[i] < nextBingo:
                    nextBingo = arr[i]

        bingo = nextBingo
        nextBingo = largest

    return arr, comparacoes, trocas