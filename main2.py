import random as rd  # Importa o módulo random com o apelido 'rd' para gerar números aleatórios

# Importa cada algoritmo de ordenação implementado na pasta 'metodos';
# todas as funções retornam uma tupla (lista_ordenada, comparações, trocas).
from metodos.bingoSort import bingo_sort        # Bingo Sort
from metodos.bubbleSort import bubble_sort      # Bubble Sort
from metodos.insertionSort import insertion_sort  # Insertion Sort
from metodos.mergeSort import merge_sort        # Merge Sort
from metodos.quickSort import quick_sort        # Quick Sort
from metodos.selectionSort import selection_sort  # Selection Sort
from metodos.shellSort import shell_sort        # Shell Sort
from metodos.radixSort import radix_sort        # Radix Sort

def matrizVetores():  # Função que cria os conjuntos de vetores aleatórios usados no benchmark
    Vetores1k = [[rd.randrange(0, 100000) for _ in range(1000)] for _ in range(3)]      # 3 vetores de 1.000 inteiros em [0, 100000)
    Vetores10k = [[rd.randrange(0, 100000) for _ in range(10000)] for _ in range(3)]    # 3 vetores de 10.000 inteiros em [0, 100000)
    Vetores50k = [[rd.randrange(0, 100000) for _ in range(50000)] for _ in range(3)]    # 3 vetores de 50.000 inteiros em [0, 100000)
    Vetores100k = [[rd.randrange(0, 100000) for _ in range(100000)] for _ in range(3)]  # 3 vetores de 100.000 inteiros em [0, 100000)

    return Vetores1k, Vetores10k, Vetores50k, Vetores100k  # Devolve os quatro conjuntos como uma tupla

def main():  # Função principal: orquestra a execução do benchmark
    conjuntos = matrizVetores()  # Obtém a tupla com os quatro conjuntos de vetores

    algoritmos = [  # Lista de pares (nome_para_exibição, função_de_ordenação) que serão testados
        ("Selection Sort", selection_sort),  # Par para o Selection Sort
        ("Insertion Sort", insertion_sort),  # Par para o Insertion Sort
        ("Shell Sort", shell_sort),          # Par para o Shell Sort
        ("Merge Sort", merge_sort),          # Par para o Merge Sort
        ("Quick Sort", quick_sort),          # Par para o Quick Sort
        ("Bingo Sort", bingo_sort),          # Par para o Bingo Sort
        ("Radix Sort", radix_sort),          # Par para o Radix Sort
    ]

    for vetores in conjuntos:  # Percorre cada conjunto (1k, 10k, 50k, 100k)
        print(f"\n=== Vetores de tamanho {len(vetores[0])} ===")  # Cabeçalho indicando o tamanho atual

        for nome, algoritmo in algoritmos:  # Para cada algoritmo da lista
            printWithTimeMedia(nome, algoritmo, vetores)  # Executa o algoritmo nos 3 vetores e imprime as métricas

        print("-" * 40)  # Separador visual entre conjuntos de tamanhos diferentes


def printWithTimeMedia(nome, algoritmo, vetores):  # Executa um algoritmo nos vetores e imprime tempo, comparações e trocas
    import time  # Importa 'time' localmente para medir o tempo de CPU

    total_tempo = 0   # Acumulador do tempo total gasto pelos 3 vetores
    total_comp = 0    # Acumulador do total de comparações
    total_trocas = 0  # Acumulador do total de trocas

    print(f"{nome} (n={len(vetores[0])})")  # Imprime o nome do algoritmo e o tamanho dos vetores

    for i, vetor in enumerate(vetores, start=1):  # Itera pelos vetores numerando-os a partir de 1
        copia = vetor.copy()  # Copia o vetor para não alterar o original (permite reutilizá-lo em outros algoritmos)

        inicio = time.process_time()  # Marca o tempo de CPU antes da ordenação
        _, comparacoes, trocas = algoritmo(copia)  # Executa o algoritmo; descarta a lista ordenada e captura métricas
        fim = time.process_time()  # Marca o tempo de CPU depois da ordenação

        tempo = fim - inicio  # Calcula a duração da ordenação em segundos

        total_tempo += tempo          # Soma o tempo deste vetor ao total
        total_comp += comparacoes     # Soma as comparações ao total
        total_trocas += trocas        # Soma as trocas ao total

        print(f"  Vetor {i}: "                          # Imprime as métricas individuais do vetor atual
              f"Tempo: {tempo:.6f}s | "                 # Tempo formatado com 6 casas decimais
              f"Comp: {comparacoes:>10} | "             # Comparações alinhadas à direita em 10 colunas
              f"Trocas: {trocas:>10}")                  # Trocas alinhadas à direita em 10 colunas

    n = len(vetores)  # Quantidade de vetores processados (usada para calcular as médias)

    print(f"  MÉDIA : "                                  # Imprime a linha de médias do algoritmo
          f"Tempo: {(total_tempo/n):.6f}s | "            # Tempo médio em segundos
          f"Comp: {int(total_comp/n):>10} | "            # Média de comparações (truncada para inteiro)
          f"Trocas: {int(total_trocas/n):>10}")          # Média de trocas (truncada para inteiro)

    print("-" * 50)  # Separador visual entre algoritmos

if __name__ == "__main__":  # Garante que o código abaixo só rode se este arquivo for executado diretamente
    main()  # Inicia o benchmark
