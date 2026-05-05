# Melhor, medio e pior caso: O(n * k) onde n é o número de elementos no array e k é o número de dígitos do maior número.
def radix_sort(arr):
    comparacoes = 0  # Radix não compara elementos diretamente
    trocas = 0

    if not arr:
        return arr, comparacoes, trocas

    max_num = max(arr)
    exp = 1 

    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            trocas += 1  # movimentação

        for i in range(n):
            arr[i] = output[i]
            trocas += 1  # cópia de volta

        exp *= 10

    return arr, comparacoes, trocas