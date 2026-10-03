import decimal
import Numero

from Numero import PRECISAO_PARTE_FRACIONARIA

from Globais import VALOR_DECIMAL_PARA_DIGITO, DIGITO_PARA_VALOR, EPS
from Utilitarios import separarNumero


def parteInteiraDecimalParaNovaBase(n: str, k: int) -> str:
    """
    Permite converter a parte inteira de um número decimal em qualquer outra base.

    Args:
        n (str): Número decimal.
        k (int): Base para a qual pretendemos converter.

    Returns:
        str: O número na nova base.
    """
    n = int(n)
    convertido = "" if n != 0 else "0"
    while n != 0:
        rest = n % k
        convertido += VALOR_DECIMAL_PARA_DIGITO[rest]
        n //= k
    return convertido[::-1]


def parteInteiraBaseAtualParaDecimal(n: str, k: int) -> str:
    """
    Permite converter um número na base especificada para decimal.

    Args:
        n (str): Número na base k
        k (int): A base do número n

    Returns:
        str: O número decimal
    """
    n_reversed = n[::-1]

    convertido = 0

    index = 0
    for value in n_reversed:
        convertido += DIGITO_PARA_VALOR[value] * (k ** index)
        index += 1
    return str(convertido)


def parteFracionariaParaNovaBase(n: str, k: int, precision: int) -> str:
    """
    Permite converter a parte fracionária de um número decimal
    noutra base qualquer com uma determinada precisão.

    Args:
        n (str): O número que vai ser convertido para a base k
        k (int): A base para a qual vamos converter o número n
        precision (int): A precisão com que pretendemos converter o número

    Returns:
        str: O número fracionário convertido na base k.
    """
    n = float("0." + n)
    fractional_part = n - int(n)
    convertido = ""
    for _ in range(precision):
        product = fractional_part * k
        digit = int(product)
        convertido += VALOR_DECIMAL_PARA_DIGITO[digit]
        fractional_part = product - int(product)
        if fractional_part - EPS <= 0:
            break
    return convertido


def parteFracionariaParaDecimal(n: str, k: int, precision: int) -> str:
    """
    Permite converter um número fracionário de qualquer base em decimal.

    Args:
        n (str): O número em qualquer base
        k (int): A base na qual está o número n.
        precision (int): A precisão com que pretendemos fazer esta conversão.

    Returns:
        str: O número fracionário convertido.
    """
    convertido = decimal.Decimal()
    current_precision = 0
    for i in range(len(n)):
        convertido += decimal.Decimal(
            DIGITO_PARA_VALOR[n[i]] * (k ** -(i + 1)))
        current_precision += 1
        if current_precision >= precision:
            break

    return str(convertido)[2:]


def converterParteInteira(numero: str, base_atual: int, base_nova: int) -> str:
    """
    Permite converter a parte inteira de um número da base atual para a nova base.

    Args:
        numero (str): O número na base base_atual
        base_atual (int): A base atual
        base_nova (int): A base nova.

    Returns:
        str: A parte inteira do número convertida na nova base.
    """
    decimal: str = parteInteiraBaseAtualParaDecimal(
        numero,
        base_atual) if base_atual != 10 else numero

    return parteInteiraDecimalParaNovaBase(decimal, base_nova)


def converterParteFracionaria(numero: str, base_atual: int, base_nova: int, precision: int = PRECISAO_PARTE_FRACIONARIA) -> str:
    """
    Permite converter a parte fracionária de um número na base atual para a nova base.

    Args:
        numero (str): O número na base base_atual
        base_atual (int): A base atual
        base_nova (int): A nova base
        precision (int, optional): A precisão com a qual se pretende obter o resultado. É PRECISION das Constants.py por defeito.

    Returns:
        str: A parte fracionária do número convertida na base_nova.
    """
    parte_fracionaria = parteFracionariaParaDecimal(
        numero, base_atual, precision) if base_atual != 10 else numero

    return parteFracionariaParaNovaBase(parte_fracionaria, base_nova, precision)


def converter(numero: Numero):
    """
    Permite converter um número na base atual para uma nova base.

    Args:
        numero (str): O número na base_atual.
        base_atual (int): A base atual.
        base_nova (int): A nova bae.

    Returns:
        str: O número convertido na base_nova.
    """
    negativo, parte_inteira, parte_fracionaria = separarNumero(
        numero.valor_atual)

    numero.valor_novo = "-" if negativo else ""

    numero.valor_novo += converterParteInteira(
        parte_inteira,
        numero.base_atual,
        numero.base_nova)

    if parte_fracionaria:
        numero.valor_novo += f".{converterParteFracionaria(
            parte_fracionaria,
            numero.base_atual,
            numero.base_nova)}"
