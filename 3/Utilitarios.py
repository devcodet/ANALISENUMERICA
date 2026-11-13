import math

def diagonalmente_dominante(m, n) -> bool:

    for i in range(0, n):
        soma = 0
        for j in range(0, n):
            soma = soma + abs(m[i][j])

        soma = soma - abs(m[i][i])

        if (abs(m[i][i]) < soma):
            return False

    return True

def norma_da_soma(matriz, n) -> float:

    norma = 0
    for i in range(0, n):
        soma = 0
        for j in range(0, n):
            soma = soma + abs(matriz[i][j])
        if (soma > norma):
            norma = soma

    return norma

def norma_euclidiana(matriz, n) -> float:

    norma = 0
    for i in range(0, n):
        soma = 0
        for j in range(0, n):
            soma = soma + (matriz[i][j] ** 2)
            if (soma > norma):
                norma = soma

    return math.sqrt(norma)

def norma_do_maximo(matriz, n) -> float:

    norma = 0
    for i in range(0, n):
        soma = 0
        for j in range(0, n):
            if (abs(matriz[i][j]) > norma):
                norma = abs(matriz[i][j])

    return norma

def calcular_erro(tipo, diferenca, valor) -> float:
    # Erro absoluto = |diferenca|; relativo = |diferenca| / |valor| (se valor != 0)
    erro = abs(diferenca)
    if tipo == "r" and valor != 0:
        erro /= abs(valor)
    return erro
