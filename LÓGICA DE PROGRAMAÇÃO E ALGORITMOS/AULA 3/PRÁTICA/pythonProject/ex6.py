def valida(pergunta, min, max):
    x = int(input(pergunta))
    while (x < min) or (x > max):
        x = int(input(pergunta))
    return x


def fatorial(n):
    """
    :param n: Calcula a fatorial do número
    :return: Retorna o valor do fatorial.
    """
    fat = 1
    if n == 0:
        return fat
    for c in range(1, n + 1):
        fat *= c
    return fat


n = valida('Digite um valor: ', 0, 99999)
print(f'{n}! é {fatorial(n)}')
