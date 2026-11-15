import math

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