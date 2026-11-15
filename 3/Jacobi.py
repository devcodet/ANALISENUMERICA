import math
import numpy
from Utilitarios import imprimir_cabecalho, imprimir_iteracao, norma_vetor, calcular_erro

def jacobi(matrizA: list[list[float]], vetorB: list[float], tipo_erro: str,
            tipo_norma: str, tol: float, max_iter: int, x0: list[float] | None = None) -> tuple[list[float], bool, int]:

    # Obter o tamanho da matriz
    n = len(vetorB)

    # Verificar se a matriz A e B têm dimensões válidas
    if n == 0 or len(matrizA[0]) != n or len(vetorB) != n:
        raise ValueError("Jacobi: dimensões inválidas. A matriz A deve ser nxn e len(b)=n.")

    if x0 is None:
        x = numpy.zeros(n)
    else:
        x = numpy.array(x0, dtype=float)

    convergiu = False
    imprimir_cabecalho("Jacobi", n)
    imprimir_iteracao(0, x, None)

    for iteracoes in range(1, max_iter+1):
        x_novo = numpy.zeros(n) # Vetor novo em cada iteração
        # Calcular a próxima aproximação
        for i in range(n):
            soma = sum(matrizA[i][j] * x[j] for j in range(n) if j != i)

            x_novo[i] = (vetorB[i] - soma) / matrizA[i][i]

        erro = calcular_erro(tipo_erro, norma_vetor(x_novo - x, tipo_norma), norma_vetor(x_novo, tipo_norma))
        imprimir_iteracao(iteracoes, x_novo, erro)

        x = x_novo # Devolve a aproximação mais recente 

        if not math.isfinite(erro):
                print("\nO método divergiu (valores infinitos ou indefinidos).")
                break

        if erro < tol:
            convergiu = True
            break

    return x.tolist(), convergiu, iteracoes