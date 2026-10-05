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
    # APLICA O MÉTODO DAS DIVISÕES SUCESSIVAS POR K.
    # OS RESTOS OBTIDOS REPRESENTAM OS DÍGITOS NA NOVA BASE DA DIREITA PARA A ESQUERDA.
    n = int(n)
    convertido = "" if n != 0 else "0"
    while n != 0:
        rest = n % k
        convertido += VALOR_DECIMAL_PARA_DIGITO[rest]
        n //= k
        
    # INVERSÃO NECESSÁRIA PORQUE A ORDEM DOS RESTOS É OPOSTA À ESCRITA POSICIONAL
    return convertido[::-1]


def parteInteiraBaseAtualParaDecimal(n: str, k: int) -> str:
    """
    Permite converter a parte inteira de um número na base k para decimal.

    Args:
        n (str): Número na base k
        k (int): A base do número n

    Returns:
        str: O número decimal
    """
    n_reversed = n[::-1]

    convertido = 0

    index = 0
    # PERCORRE OS DÍGITOS DA DIREITA PARA A ESQUERDA (DO MENOS PARA O MAIS SIGNIFICATIVO)
    # MULTIPLICA O VALOR DE CADA DÍGITO PELA BASE K ELEVADA À RESPETIVA POSIÇÃO.
    for value in n_reversed:
        convertido += DIGITO_PARA_VALOR[value] * (k ** index)
        index += 1
    return str(convertido)


def parteFracionariaDecimalParaNovaBase(n: str, k: int, precision: int) -> str:
    """
    Permite converter a parte fracionária de um número decimal
    noutra base k com uma determinada precisão.

    Args:
        n (str): O número que vai ser convertido para a base k
        k (int): A base para a qual vamos converter o número n
        precision (int): A precisão com que pretendemos converter o número

    Returns:
        str: O número fracionário convertido na base k.
    """
    # APLICA O MÉTODO DAS MULTIPLICAÇÕES SUCESSIVAS PELA BASE.
    # O PROCESSO TERMINA AO ATINGIR A PRECISÃO MÁXIMA OU SE A FRAÇÃO FOR NULA (DENTRO DA TOLERÂNCIA EPS).
    n = float("0." + n)
    fractional_part = n - int(n)
    convertido = ""
    for _ in range(precision):
        product = fractional_part * k
        digit = int(product)
        convertido += VALOR_DECIMAL_PARA_DIGITO[digit]
        fractional_part = product - int(product)

        # CRITÉRIO DE PARAGEM - INTERROMPE SE A PARTE FRACIONÁRIA FOR PRATICAMENTE NULA
        if fractional_part - EPS <= 0:
            break
    return convertido


def parteFracionariaBaseAtualParaDecimal(n: str, k: int, precision: int) -> str:
    """
    Permite converter um número fracionário de uma qualquer base k em decimal.

    Args:
        n (str): O número em qualquer base
        k (int): A base na qual está o número n.
        precision (int): A precisão com que pretendemos fazer esta conversão.

    Returns:
        str: O número fracionário convertido.
    """
    # PERCORRE OS DÍGITOS FRACIONÁRIOS DA ESQUERDA PARA A DIREITA
    # MULTIPLICA O VALOR DE CADA DÍGITO PELA BASE K ELEVADA À RESPETIVA POSIÇÃO NEGATIVA. (PESO POSICIONAL: K^(-1), K^(-2), ...)
    convertido = decimal.Decimal()
    current_precision = 0
    for i in range(len(n)):
        convertido += decimal.Decimal(
            DIGITO_PARA_VALOR[n[i]] * (k ** -(i + 1)))
        current_precision += 1
        if current_precision >= precision:
            break

    # DEVOLVE APENAS OS DÍGITOS DECIMAIS, REMOVENDO OS PRIMEIROS DOIS CARACTERES ('0.')        
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
    # SE JÁ ESTIVER NA BASE 10 EVITA CÁLCULOS DESNECESSÁRIOS - SENÃO, CONVERTE DA BASE ATUAL PARA DECIMAL
    decimal: str = parteInteiraBaseAtualParaDecimal(
        numero,
        base_atual) if base_atual != 10 else numero
    
    # CONVERTE O VALOR INTERMÉDIO EM DECIMAL PARA A NOVA BASE
    return parteInteiraDecimalParaNovaBase(decimal, base_nova)


def converterParteFracionaria(numero: str, base_atual: int, base_nova: int, precision: int = PRECISAO_PARTE_FRACIONARIA) -> str:
    """
    Permite converter a parte fracionária de um número na base atual para a nova base.

    Args:
        numero (str): O número na base base_atual
        base_atual (int): A base atual
        base_nova (int): A nova base
        precision (int): A precisão com a qual se pretende obter o resultado. É PRECISION de Numero.py por defeito.

    Returns:
        str: A parte fracionária do número convertida na base nova.
    """
    # OBTÉM A PARTE FRACIONÁRIA EM DECIMAL. CASO A BASE ATUAL JÁ SEJA 10, EVITA CÁLCULOS DESNECESSÁRIOS.
    parte_fracionaria = parteFracionariaBaseAtualParaDecimal(
        numero, base_atual, precision) if base_atual != 10 else numero
    
    # CONVERTE O VALOR INTERMÉDIO EM DECIMAL PARA A NOVA BASE COM A PRECISÃO DESEJADA
    return parteFracionariaDecimalParaNovaBase(parte_fracionaria, base_nova, precision)


def converter(numero: Numero):
    """
    Permite converter um número na base atual para uma nova base.

    Args:
        numero (Numero): OBJETO CONTENDO O VALOR ORIGINAL E AS RESPETIVAS BASES.

    Returns:
        str: O número convertido na base_nova.
    """
    # DECOMPÕE O VALOR ORIGINAL EM SINAL, PARTE INTEIRA E PARTE FRACIONÁRIA
    negativo, parte_inteira, parte_fracionaria = separarNumero(
        numero.valor_atual)

    # DEFINE O SINAL
    numero.valor_novo = "-" if negativo else ""

    #CONVERTE A PARTE INTEIRA PARA A NOVA BASE
    numero.valor_novo += converterParteInteira(
        parte_inteira,
        numero.base_atual,
        numero.base_nova)
    
    # CONVERTE A PARTE FRACIONÁRIA PARA A NOVA BASE, SE EXISTIR
    if parte_fracionaria:
        numero.valor_novo += f".{converterParteFracionaria(
            parte_fracionaria,
            numero.base_atual,
            numero.base_nova)}"
