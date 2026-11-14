import numpy
from Utilitarios import norma_vetor, calcular_erro

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
        x = x0

    x_novo = numpy.zeros(n)
    convergiu = False

    for iteracoes in range(1, max_iter+1):
        # Calcular a próxima aproximação
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += matrizA[i][j] * x[j]
            x_novo[i] = (vetorB[i] - soma) / matrizA[i][i]

        diferenca = numpy.sum(numpy.abs(x_novo - x))

        erro = calcular_erro(tipo_erro, norma_vetor(diferenca, tipo_norma), norma_vetor(x_novo, tipo_norma))

        if erro < tol:
            convergiu = True
            break

        x = x_novo.copy()

    return x, convergiu, iteracoes