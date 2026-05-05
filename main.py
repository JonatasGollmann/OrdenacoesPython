import random as rd  # Importa o módulo random com o apelido 'rd' para gerar valores aleatórios

# Importa cada algoritmo de ordenação implementado na pasta 'metodos'.
from metodos.bingoSort import bingo_sort        # Bingo Sort
from metodos.bubbleSort import bubble_sort      # Bubble Sort
from metodos.insertionSort import insertion_sort  # Insertion Sort
from metodos.mergeSort import merge_sort        # Merge Sort
from metodos.quickSort import quick_sort        # Quick Sort
from metodos.selectionSort import selection_sort  # Selection Sort
from metodos.shellSort import shell_sort        # Shell Sort
from metodos.radixSort import radix_sort        # Radix Sort (importado mas não usado em main())

def vetores():  # Define a função que devolve os vetores de teste
    # Para testar: Lista de números em ordem aleatória.
    vetor1 = [8, 5, 1, 7, 9, 4, 10, 3, 6, 2]  # Caso comum: elementos fora de ordem
    # Para testar: Uma lista que já está ordenada.
    vetor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Caso de melhor desempenho para vários algoritmos
    # Para testar: Uma lista classificada em ordem decrescente.
    vetor3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Caso de pior desempenho para vários algoritmos
    # Para testar: Uma lista contendo elementos repetidos.
    vetor4 = [8, 5, 1, 7, 9, 4, 10, 3, 6, 2, 8, 5, 1]  # Verifica como o algoritmo trata duplicatas
    # Para testar: Uma lista vazia.
    vetor5 = []  # Caso de borda: lista sem elementos
    # Para testar: Uma lista contendo apenas um elemento.
    vetor6 = [5]  # Caso de borda: lista com um único elemento
    # Para testar: Uma lista contendo um elemento repetido muitas vezes.
    vetor7 = [6, 9, 6, 7, 6, 5, 6, 6, 2, 6]  # Caso favorável ao Bingo Sort
    # Para testar: Uma lista longa.
    vetor8 = [rd.randrange(0, 1000) for _ in range(100)]  # 100 inteiros aleatórios em [0, 1000)
    return vetor1, vetor2, vetor3, vetor4, vetor5, vetor6, vetor7, vetor8  # Retorna todos os vetores como tupla

def main():  # Função principal: executa cada algoritmo sobre cada vetor de teste
    for vetor in vetores():  # Itera sobre cada um dos vetores de teste
        print(f"Original vetor: {vetor}")  # Mostra o vetor original antes de ordenar
        printWithTime("Bubble Sort", bubble_sort, vetor)        # Executa e cronometra o Bubble Sort
        printWithTime("Selection Sort", selection_sort, vetor)  # Executa e cronometra o Selection Sort
        printWithTime("Insertion Sort", insertion_sort, vetor)  # Executa e cronometra o Insertion Sort
        printWithTime("Shell Sort", shell_sort, vetor)          # Executa e cronometra o Shell Sort
        printWithTime("Merge Sort", merge_sort, vetor)          # Executa e cronometra o Merge Sort
        printWithTime("Quick Sort", quick_sort, vetor)          # Executa e cronometra o Quick Sort
        printWithTime("Bingo Sort", bingo_sort, vetor)          # Executa e cronometra o Bingo Sort

        print("-" * 40)  # Separador visual entre os vetores

def printWithTime(nomeMetodo, method, vetor):  # Mede o tempo de execução de um método de ordenação
    import time  # Importa 'time' localmente para acessar time.time()
    start_time = time.time()  # Marca o instante antes da ordenação (relógio de parede)
    sorted_vetor = method(vetor.copy())  # Ordena uma cópia do vetor para preservar o original
    end_time = time.time()  # Marca o instante após a ordenação
    print(f"{nomeMetodo}: {end_time - start_time:.6f} seconds.")  # Imprime o tempo decorrido com 6 casas decimais
    return sorted_vetor  # Devolve o vetor ordenado

    # import timeit
    # runs = 1000
    # exec_time = timeit.timeit(lambda: method(vetor.copy()), number=runs) / runs

    # sorted_vetor = method(vetor.copy())
    # print(f"{nomeMetodo}: {exec_time:.6f} seconds (média de {runs} execuções).")
    # return sorted_vetor

if __name__ == "__main__":  # Garante que main() só seja chamada quando o arquivo for executado diretamente
    main()  # Inicia a execução dos testes
