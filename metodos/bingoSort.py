# Bingo Sort é um algoritmo de ordenação que é uma variação do Selection Sort. 
# Ele é eficiente para ordenar listas com muitos elementos repetidos, 
# pois ele move todos os elementos iguais para a posição correta em uma única passagem.
# BIG-0 O(n * m) onde n é o número de elementos na lista e m é o número de elementos únicos.
# O(n + m^2) no melhor caso

def bingo_sort(arr):
    size = len(arr)
    if size == 0:
        return arr
    
    bingo = min(arr)
    
    largest = max(arr)
    nextBingo = largest
    nextPos = 0
    while bingo < nextBingo:
    
        startPos = nextPos
        for i in range(startPos, size):
            if arr[i] == bingo:
                arr[i], arr[nextPos] = arr[nextPos], arr[i]
                nextPos += 1
            elif arr[i] < nextBingo:
                nextBingo = arr[i]
        bingo = nextBingo
        nextBingo = largest
    return arr