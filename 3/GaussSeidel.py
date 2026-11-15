import math
import numpy
from Utilitarios import imprimir_cabecalho, imprimir_iteracao, norma_vetor, calcular_erro

def gauss_seidel(matrizA: list[list[float]], vetorB: list[float], tipo_erro: str, 
                tipo_norma: str, tol: float, max_iter: int, x0: list[float] | None = None) -> tuple[list[float], bool, int]:
            
    n = len(vetorB)

    # Verificar se a matriz A e B têm dimensões válidas
    if n == 0 or len(matrizA[0]) != n or len(vetorB) != n:
        raise ValueError("Gauss-Seidel: dimensões inválidas. A matriz A deve ser nxn e len(b)=n.")

    if x0 is None:
        x = numpy.zeros(n)
    else:
        x = numpy.array(x0, dtype=float)

    convergiu = False
    imprimir_cabecalho("Gauss-Seidel", n)
    imprimir_iteracao(0, x, None)

    for iteracoes in range(1, max_iter+1):
        x_ant = x.copy()
        # Calcular a próxima aproximação
        for i in range(n):
            s1 = sum(matrizA[i][j] * x[j] for j in range(i)) # Já atualizados (iteração k)
            s2 = sum(matrizA[i][j] * x_ant[j] for j in range(i + 1, n)) # Iteração k-1
            x[i] = (vetorB[i] - s1 - s2) / matrizA[i][i]

        erro = calcular_erro(tipo_erro, norma_vetor(x - x_ant, tipo_norma), norma_vetor(x, tipo_norma))
        imprimir_iteracao(iteracoes, x, erro)

        if not math.isfinite(erro):
                print("\nO método divergiu (valores infinitos ou indefinidos).")
                break

        if erro < tol:
            convergiu = True
            break

        x_ant = x.copy()

    return x.tolist(), convergiu, iteracoes