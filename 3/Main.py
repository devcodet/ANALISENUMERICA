from Leitura import ler_tamanho_matriz, ler_matriz, ler_vetor, ler_metodo, ler_tolerancia_iteracoes
from Utilitarios import verificar_diagonalmente_dominante, verificar_determinante_zero, imprimir_resultado
from Jacobi import jacobi
from GaussSeidel import gauss_seidel

def analisar_sistema_de_equacoes_lineares(matriz, n) -> bool:
    # Devolve False se os métodos não puderem ser aplicados
    
    det, singular = verificar_determinante_zero(matriz, n)
    if singular:
        print("\nAviso: o determinante de A é nulo (matriz singular): o sistema não tem solução única.")
        return False
    else:
        print(f"\nDeterminante da matriz A = {det:.6g}: o sistema tem solução única." 
            "Podemos aplicar os métodos iterativos de Jacobi e Gauss-Seidel, sem garantias de convergência.")

    if verificar_diagonalmente_dominante(matriz, n):
        print("\nA matriz A é estritamente diagonalmente dominante: a convergência dos métodos é garantida.")
    else:
        print("\nA matriz A não é estritamente diagonalmente dominante: a convergência dos métodos não está garantida.")

    # Verificar que não há valores nulos na diagonal da matriz A
    for i in range(n):
        if abs(matriz[i][i]) == 0:
            print("A diagonal da matriz A não pode conter valores nulos. Os métodos não são aplicáveis.")
            return False

    return True

def main():
    print("=== Resolução de sistemas de equações lineares (AX = B)"
        " pelo método iterativo de Jacobi e Gauss-Seidel ===")

    while True:
        n = ler_tamanho_matriz()
        A = ler_matriz(n)
        B = ler_vetor(n)
        x0 = ler_vetor(n)
        metodo = ler_metodo()
        tipo_erro, tipo_norma, tol, max_iter = ler_tolerancia_iteracoes()

        if analisar_sistema_de_equacoes_lineares(A, n):
            if metodo == "Jacobi":
                x, convergiu, iteracoes = jacobi(A, B, tipo_erro, tipo_norma, tol, max_iter, x0)
            else:
                x, convergiu, iteracoes = gauss_seidel(A, B, tipo_erro, tipo_norma, tol, max_iter, x0)

            if convergiu:
                print(f"\nO método convergiu em {iteracoes} iterações.")
            else:
                print(f"\nO número máximo de iterações: {max_iter}, foi excedido sem convergência.")

            imprimir_resultado(metodo, convergiu, x, iteracoes, max_iter, tol)

if __name__ == "__main__":
    main()
