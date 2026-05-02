import random as rd

from metodos.bingoSort import bingo_sort
from metodos.bubbleSort import bubble_sort
from metodos.insertionSort import insertion_sort
from metodos.mergeSort import merge_sort
from metodos.quickSort import quick_sort
from metodos.selectionSort import selection_sort
from metodos.shellSort import shell_sort
from metodos.radixSort import radix_sort

def matrizVetores():
    Vetores1k = [[rd.randrange(0, 100000) for _ in range(1000)] for _ in range(3)]
    Vetores10k = [[rd.randrange(0, 100000) for _ in range(10000)] for _ in range(3)]
    Vetores50k = [[rd.randrange(0, 100000) for _ in range(50000)] for _ in range(3)]
    Vetores100k = [[rd.randrange(0, 100000) for _ in range(100000)] for _ in range(3)]
    
    return Vetores1k, Vetores10k, Vetores50k, Vetores100k

def main():
    conjuntos = matrizVetores()

    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Shell Sort", shell_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Bingo Sort", bingo_sort),
        ("Radix Sort", radix_sort),
    ]

    for vetores in conjuntos:
        print(f"\n=== Vetores de tamanho {len(vetores[0])} ===")

        for nome, algoritmo in algoritmos:
            print(f"\n>> {nome}")

            for vetor in vetores:
                copia = vetor.copy()
                printWithTime(nome, algoritmo, copia)

        print("-" * 40)

def printWithTime(nomeMetodo, method, vetor):
    import time
    start_time = time.perf_counter()
    sorted_vetor = method(vetor.copy())
    end_time = time.perf_counter()
    print(f"{nomeMetodo}: {end_time - start_time:.6f} seconds.")

    # import timeit
    # runs = 1000
    # exec_time = timeit.timeit(lambda: method(vetor.copy()), number=runs) / runs

    # sorted_vetor = method(vetor.copy())
    # print(f"{nomeMetodo}: {exec_time:.6f} seconds (média de {runs} execuções).")
    # return sorted_vetor

if __name__ == "__main__":
    main()