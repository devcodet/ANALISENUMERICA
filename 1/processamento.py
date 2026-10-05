import decimal
import Numero

from Numero import PRECISAO_PARTE_FRACIONARIA

from Globais import VALOR_DECIMAL_PARA_DIGITO, DIGITO_PARA_VALOR, EPS
from Utilitarios import separarNumero

# CONVERTER PARTE INTEIRA DO NUMERO EM DECIMAL PARA OUTRA NOVA BASE


def parteInteiraDecimalParaNovaBase(numero_decimal: str, base_nova: int) -> str:
    # APLICA O MÉTODO DAS DIVISÕES SUCESSIVAS POR K.
    # OS RESTOS OBTIDOS REPRESENTAM OS DÍGITOS NA NOVA BASE DA DIREITA PARA A ESQUERDA.
    numero_decimal = int(numero_decimal)
    convertido = "" if numero_decimal != 0 else "0"
    while numero_decimal != 0:
        rest = numero_decimal % base_nova
        convertido += VALOR_DECIMAL_PARA_DIGITO[rest]
        numero_decimal //= base_nova

    # INVERSÃO NECESSÁRIA PORQUE A ORDEM DOS RESTOS É OPOSTA À ESCRITA POSICIONAL
    return convertido[::-1]

# CONVERTER PARTE INTEIRA DO NUMERO NUMA BASE PARA DECIMAL


def parteInteiraBaseAtualParaDecimal(numero_na_base: str, base: int) -> str:
    numero_revertido = numero_na_base[::-1]

    convertido = 0

    index = 0
    # PERCORRE OS DÍGITOS DA DIREITA PARA A ESQUERDA (DO MENOS PARA O MAIS SIGNIFICATIVO)
    # MULTIPLICA O VALOR DE CADA DÍGITO PELA BASE K ELEVADA À RESPETIVA POSIÇÃO.
    for valor in numero_revertido:
        convertido += DIGITO_PARA_VALOR[valor] * (base ** index)
        index += 1
    return str(convertido)

# CONVERTER PARTE FRACIONARIA DE UM DECIMAL PARA NOVA BASE COM PRECISAO DESEJADA


def parteFracionariaDecimalParaNovaBase(numero_para_converter: str, base_nova: int, precisao: int) -> str:

    # APLICA O MÉTODO DAS MULTIPLICAÇÕES SUCESSIVAS PELA BASE.
    # O PROCESSO TERMINA AO ATINGIR A PRECISÃO MÁXIMA OU SE A FRAÇÃO FOR NULA (DENTRO DA TOLERÂNCIA EPS).
    numero_para_converter = float("0." + numero_para_converter)
    parte_fracionaria = numero_para_converter - int(numero_para_converter)
    convertido = ""
    for _ in range(precisao):
        produto = parte_fracionaria * base_nova
        digito = int(produto)
        convertido += VALOR_DECIMAL_PARA_DIGITO[digito]
        parte_fracionaria = produto - int(produto)

        # CRITÉRIO DE PARAGEM - INTERROMPE SE A PARTE FRACIONÁRIA FOR PRATICAMENTE NULA
        if parte_fracionaria - EPS <= 0:
            break
    return convertido

# CONVERTER FRACIONARIO DE UMA BASE PARA DECIMAL COM PRECISAO DESEJADA


def parteFracionariaBaseAtualParaDecimal(numero_na_base: str, base_atual: int, precisao: int) -> str:
    # PERCORRE OS DÍGITOS FRACIONÁRIOS DA ESQUERDA PARA A DIREITA
    # MULTIPLICA O VALOR DE CADA DÍGITO PELA BASE K ELEVADA À RESPETIVA POSIÇÃO NEGATIVA. (PESO POSICIONAL: K^(-1), K^(-2), ...)
    convertido = decimal.Decimal()
    precisao_atual = 0
    for i in range(len(numero_na_base)):
        convertido += decimal.Decimal(
            DIGITO_PARA_VALOR[numero_na_base[i]] * (base_atual ** -(i + 1)))
        precisao_atual += 1
        if precisao_atual >= precisao:
            break

    # DEVOLVE APENAS OS DÍGITOS DECIMAIS, REMOVENDO OS PRIMEIROS DOIS CARACTERES ('0.')
    return str(convertido)[2:]

# CONVERTER PARTE INTEIRA DA BASE ATUAL PARA NOVA BASE


def converterParteInteira(numero: str, base_atual: int, base_nova: int) -> str:
    # SE JÁ ESTIVER NA BASE 10 EVITA CÁLCULOS DESNECESSÁRIOS - SENÃO, CONVERTE DA BASE ATUAL PARA DECIMAL
    decimal: str = parteInteiraBaseAtualParaDecimal(
        numero,
        base_atual) if base_atual != 10 else numero

    # CONVERTE O VALOR INTERMÉDIO EM DECIMAL PARA A NOVA BASE
    return parteInteiraDecimalParaNovaBase(decimal, base_nova)

# CONVERTER PARTE FRACIONARIA DA BASE ATUAL PARA NOVA BASE COM PRECISAO DESEJADA


def converterParteFracionaria(numero: str, base_atual: int, base_nova: int, precisao: int = PRECISAO_PARTE_FRACIONARIA) -> str:
    # OBTÉM A PARTE FRACIONÁRIA EM DECIMAL. CASO A BASE ATUAL JÁ SEJA 10, EVITA CÁLCULOS DESNECESSÁRIOS.
    parte_fracionaria = parteFracionariaBaseAtualParaDecimal(
        numero, base_atual, precisao) if base_atual != 10 else numero

    # CONVERTE O VALOR INTERMÉDIO EM DECIMAL PARA A NOVA BASE COM A PRECISÃO DESEJADA
    return parteFracionariaDecimalParaNovaBase(parte_fracionaria, base_nova, precisao)


# CONVERTER NUMERO DE UMA BASE PARA OUTRA NOVA BASE
def converter(numero: Numero):
    # DECOMPÕE O VALOR ORIGINAL EM SINAL, PARTE INTEIRA E PARTE FRACIONÁRIA
    negativo, parte_inteira, parte_fracionaria = separarNumero(
        numero.valor_atual)

    # DEFINE O SINAL
    numero.valor_novo = "-" if negativo else ""

    # CONVERTE A PARTE INTEIRA PARA A NOVA BASE
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
