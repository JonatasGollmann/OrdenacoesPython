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
            printWithTimeMedia(nome, algoritmo, vetores)

        print("-" * 40)


def printWithTimeMedia(nome, algoritmo, vetores):
    import time
    
    total_tempo = 0
    total_comp = 0
    total_trocas = 0

    print(f"{nome} (n={len(vetores[0])})")

    for i, vetor in enumerate(vetores, start=1):
        copia = vetor.copy()

        inicio = time.process_time()
        _, comparacoes, trocas = algoritmo(copia)
        fim = time.process_time()

        tempo = fim - inicio

        total_tempo += tempo
        total_comp += comparacoes
        total_trocas += trocas

        print(f"  Vetor {i}: "
              f"Tempo: {tempo:.6f}s | "
              f"Comp: {comparacoes:>10} | "
              f"Trocas: {trocas:>10}")

    n = len(vetores)

    print(f"  MÉDIA : "
          f"Tempo: {(total_tempo/n):.6f}s | "
          f"Comp: {int(total_comp/n):>10} | "
          f"Trocas: {int(total_trocas/n):>10}")
    
    print("-" * 50)

if __name__ == "__main__":
    main()