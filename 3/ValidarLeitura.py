import math
from sympy import sympify, log, sin, cos, tan, sec, csc, cot, sqrt, exp, E, pi

FUNCOES = {
    "sin": sin, "sen": sin, "seno": sin, "sine": sin,
    "cos": cos, "coseno": cos, "cosseno": cos, "cosine": cos,
    "tan": tan, "tg": tan, "tangente": tan, "tangent": tan,
    "sec": sec, "secante": sec, "secant": sec,
    "csc": csc, "cosec": csc, "cossecante": csc, "cosecante": csc, "cosecant": csc,
    "cot": cot, "ctg": cot, "cotangente": cot, "cotangent": cot,
    "ln": log, "log": log, "logn": log,
    "log10": lambda x: log(x, 10), "log2": lambda x: log(x, 2),
    "raiz": sqrt, "sqrt": sqrt, "exp": exp,
    "e": E, "pi": pi,
}

def converter_para_float(texto: str) -> float:

    original_texto = texto
    texto = texto.strip().lower().replace("π", "pi").replace("^", "**")
    if "(" not in texto:  # Vírgula decimal (No caso de não haver funções)
        texto = texto.replace(",", ".")
    
    try:
        numero = float(sympify(texto, locals=FUNCOES).evalf())
    except Exception:
        raise ValueError(f"'{original_texto}' não é um número ou expressão válida.")
    if not math.isfinite(numero):
        raise ValueError(f"'{original_texto}' não dá um número finito.")
    return numero
    
def validar_numero(valor: str) -> None:
    try:
        valor = float(valor)
    except ValueError:
        raise ValueError(f"Erro: '{valor}' não é um número válido.")
    if not math.isfinite(valor):
        raise ValueError(f"Erro: '{valor}' não é um número finito.")

def validar_vetor(vetor: list[float], tamanho: int) -> bool:

    if len(vetor) != tamanho:
        raise ValueError(f"Erro: O vetor deve ter exatamente {tamanho} elementos. Tamanho atual: {len(vetor)}.")

    for valor in vetor:
        validar_numero(str(valor))
    return True

def validar_matriz(matriz: list[list[float]], n: int) -> bool:

    if len(matriz) != n:
        raise ValueError(f"Erro: A matriz deve ter exatamente {n} linhas. Linhas atuais: {len(matriz)}.")

    for i, linha in enumerate(matriz):
        if len(linha) != n:
            raise ValueError(f"Erro: A linha {i + 1} da matriz deve ter exatamente {n} colunas. Colunas atuais: {len(linha)}.")
        for valor in linha:
            validar_numero(str(valor))
    return True

def validar_tamanho_matriz(n: str) -> int:
    n = n.strip()

    if not n.isdigit():
        raise ValueError("Erro: Insira apenas números inteiros positivos.")

    n = int(n)

    if n <= 0:
        raise ValueError("Erro: O número de linhas e colunas deve ser maior que zero.")

    return n