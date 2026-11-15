import math
from sympy import Matrix, Rational

def verificar_diagonalmente_dominante(matriz, n) -> bool:

    for i in range(0, n):
        soma = 0
        for j in range(0, n):
            soma = soma + abs(matriz[i][j])

        soma = soma - abs(matriz[i][i])

        if (abs(matriz[i][i]) <= soma):
            return False

    return True

def verificar_determinante_zero(matriz: list[list[float]], n: int) -> tuple[float, bool]:

    M = Matrix([[Rational(repr(float(matriz[i][j]))) for j in range(n)] for i in range(n)])
    det = M.det()
    return float(det), det == 0

def norma_vetor(vetor, tipo_norma) -> float:

    if tipo_norma == "s":
        return sum(abs(x) for x in vetor)
    elif tipo_norma == "e":
        return math.sqrt(sum(x ** 2 for x in vetor))
    elif tipo_norma == "m":
        return max(abs(x) for x in vetor)
    else:
        raise ValueError("Tipo de norma inválido. Use 's', 'e' ou 'm'.")    

def calcular_erro(tipo, diferenca, valor) -> float:

    # Erro absoluto = |diferenca|; relativo = |diferenca| / |valor| (se valor != 0)
    erro = abs(diferenca)
    if tipo == "r" and valor != 0:
        erro /= abs(valor)
    return erro

def formatar_vetor(x) -> str:
    return "[" + ", ".join(f"{v:.8f}" for v in x) + "]"

def imprimir_resultado(metodo, convergiu, x, iteracoes, max_iter, tol) -> None:
    print()
    if convergiu:
        print(f"[{metodo}] Tolerância {tol:g} atingida ao fim de {iteracoes} iterações.")
        print(f"Solução aproximada: {formatar_vetor(x)}")
    else:
        print(f"[{metodo}] Número máximo de iterações ({max_iter}) excedido sem convergência (tolerância {tol:g} não atingida).")
        print(f"Última aproximação: {formatar_vetor(x)}")

def imprimir_cabecalho(metodo, n) -> None:
    print(f"\n===== Método iterativo de {metodo} =====")
    print(f"{'k':>4} | {'X(k)':<{max(4, 12 * n)}} | Erro")

def imprimir_iteracao(k, x, erro) -> None:
    texto_erro = "-" if erro is None else f"{erro:.6e}"
    print(f"{k:>4} | {formatar_vetor(x)} | {texto_erro}")
