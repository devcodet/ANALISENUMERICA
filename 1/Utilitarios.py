from Globais import VALOR_DECIMAL_PARA_DIGITO


def validacaoCaracteres(numero: str, base: int) -> bool:
    """
    Valida se todos os caracteres do número estão dentro do conjunto permitido para a base especificada.

    Args:
        numero (str): O número a ser validado.
        base (int): A base numérica para validação.

    Returns:
        bool: True se todos os caracteres forem válidos, False caso contrário.
    """
    caracteres_validos = set(VALOR_DECIMAL_PARA_DIGITO[i] for i in range(base))

    contador_ponto = 0
    contador_sinal = 0

    for i, char in enumerate(numero):
        if char == '.':
            contador_ponto += 1
            if contador_ponto > 1:
                return False
            continue
        if char in ['+', '-']:
            contador_sinal += 1
            if contador_sinal > 1 or i != 0:
                return False
            continue
        if char not in caracteres_validos:
            return False
    return True


def separarNumero(numero: str) -> tuple[bool, str, str]:
    """
    Separa o número em parte inteira e parte decimal.

    Args:
        numero (str): O número a ser separado.

    Returns:
        tuple: Um tuplo com um booleano que indica se o número é negativo, e contendo a parte inteira e a parte decimal do número.
    """
    # É UM NUMERO NEGATIVO?
    numero_negativo = numero.startswith("-")

    # TEMOS QUE REMOVER PRIMEIRO O SINAL
    if numero.startswith(("+", "-")):
        numero = numero[1:]

    # SEPARAR PARTE INTEIRA DA PARTE FRACIONARIA
    if '.' in str(numero):
        parte_inteira, parte_fracionaria = numero.split('.')
    else:
        parte_inteira, parte_fracionaria = numero, ''

    return numero_negativo, parte_inteira, parte_fracionaria
