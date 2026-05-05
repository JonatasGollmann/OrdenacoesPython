# Melhor, medio e pior caso: O(n * k) onde n é o número de elementos no array e k é o número de dígitos do maior número.
def radix_sort(arr):  # Ordena 'arr' in-place usando Radix Sort (LSD, base 10)
    comparacoes = 0  # Radix não compara elementos diretamente
    trocas = 0       # Contador de movimentações de elementos

    if not arr:  # Caso de lista vazia
        return arr, comparacoes, trocas  # Retorna sem fazer nada

    max_num = max(arr)  # Maior valor da lista — define quantos dígitos processar
    exp = 1  # Expoente do dígito atual (1 = unidades, 10 = dezenas, ...)

    while max_num // exp > 0:  # Continua enquanto houver dígitos a processar
        n = len(arr)  # Tamanho da lista
        output = [0] * n   # Lista auxiliar para a saída desta passagem
        count = [0] * 10   # Contagem para cada dígito (0..9) — counting sort

        for num in arr:  # Conta a frequência de cada dígito na posição 'exp'
            index = (num // exp) % 10  # Extrai o dígito correspondente
            count[index] += 1  # Incrementa a contagem

        for i in range(1, 10):  # Soma cumulativa para obter posições finais
            count[i] += count[i - 1]  # count[i] passa a indicar a última posição do dígito i

        for i in range(n - 1, -1, -1):  # Percorre 'arr' do fim para o início (estabilidade)
            index = (arr[i] // exp) % 10  # Dígito do elemento atual
            output[count[index] - 1] = arr[i]  # Coloca-o na posição correta em 'output'
            count[index] -= 1  # Decrementa a posição para o próximo elemento com mesmo dígito
            trocas += 1  # movimentação

        for i in range(n):  # Copia 'output' de volta para 'arr'
            arr[i] = output[i]  # Substitui o elemento original
            trocas += 1  # cópia de volta

        exp *= 10  # Avança para o próximo dígito (mais significativo)

    return arr, comparacoes, trocas  # Retorna a lista ordenada e as métricas
