from Globais import VALOR_DECIMAL_PARA_DIGITO

# VALIDA SE TODOS OS CARATERES SAO VALIDOS NUM CONJUNTO PERMITIDO PARA A BASE ESCOLHIDA


def validacaoCaracteres(numero: str, base: int) -> bool:
    # DEFINE O CONJUNTO DE CARACTERES PERMITIDOS PARA A BASE ESPECIFICADA
    caracteres_validos = set(VALOR_DECIMAL_PARA_DIGITO[i] for i in range(base))

    contador_ponto = 0
    contador_sinal = 0

    # PERCORRE CADA CARACTERE DO NÚMERO, VALIDANDO SINTAXE E PERTENÇA À BASE
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

# SEPARA O NUMERO NUMA PARTE INTEIRA E NUMA PARTE FRACIONARIA


def separarNumero(numero: str) -> tuple[bool, str, str]:

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
