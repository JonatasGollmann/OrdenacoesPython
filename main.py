import random as rd

from metodos.bingoSort import bingo_sort
from metodos.bubbleSort import bubble_sort
from metodos.insertionSort import insertion_sort
from metodos.mergeSort import merge_sort
from metodos.quickSort import quick_sort
from metodos.selectionSort import selection_sort
from metodos.shellSort import shell_sort
from metodos.radixSort import radix_sort

def vetores():
    # Para testar: Lista de números em ordem aleatória.
    vetor1 = [8, 5, 1, 7, 9, 4, 10, 3, 6, 2]
    # Para testar: Uma lista que já está ordenada.
    vetor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Para testar: Uma lista classificada em ordem decrescente.
    vetor3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # Para testar: Uma lista contendo elementos repetidos.
    vetor4 = [8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1]
    # Para testar: Uma lista vazia.
    vetor5 = []
    # Para testar: Uma lista contendo apenas um elemento.
    vetor6 = [5]
    # Para testar: Uma lista contendo um elemento repetido muitas vezes.
    vetor7 = [6, 9, 6, 7, 6, 5, 6, 6, 2, 6]
    # Para testar: Uma lista longa.
    vetor8 = [rd.randrange(0, 1000) for _ in range(100)]
    return vetor1, vetor2, vetor3, vetor4, vetor5, vetor6, vetor7, vetor8

def main():
    for vetor in vetores():
        print(f"Original vetor: {vetor}")
        printWithTime("Bubble Sort", bubble_sort, vetor)
        printWithTime("Selection Sort", selection_sort, vetor)
        printWithTime("Insertion Sort", insertion_sort, vetor)
        printWithTime("Shell Sort", shell_sort, vetor)
        printWithTime("Merge Sort", merge_sort, vetor)
        printWithTime("Quick Sort", quick_sort, vetor)
        printWithTime("Bingo Sort", bingo_sort, vetor)

        print("-" * 40)

def printWithTime(nomeMetodo, method, vetor):
    import time
    start_time = time.time()
    sorted_vetor = method(vetor.copy())
    end_time = time.time()
    print(f"{nomeMetodo}: {end_time - start_time:.6f} seconds.")
    return sorted_vetor

    # import timeit
    # runs = 1000
    # exec_time = timeit.timeit(lambda: method(vetor.copy()), number=runs) / runs

    # sorted_vetor = method(vetor.copy())
    # print(f"{nomeMetodo}: {exec_time:.6f} seconds (média de {runs} execuções).")
    # return sorted_vetor

if __name__ == "__main__":
    main()