from sympy import lambdify, diff
from leitura import x, ler_funcao, ler_intervalo, ler_metodo, ler_precisao_iteracoes
from bisseccao import bissecao
from secante import secante
from newton import newton
from utilitarios import casas_decimais


def main():
    f, expressao = ler_funcao()
    a, b = ler_intervalo()
    metodo = ler_metodo()
    tipo, erro, max_iter = ler_precisao_iteracoes()

    resultado = None

    print(f"Método -> {metodo.capitalize()}")

    try:
        if metodo == "bissecao":
            resultado = bissecao(f, a, b, tipo, erro, max_iter)
        elif metodo == "newton":
            df  = lambdify(x, diff(expressao, x), "math")  # Derivada da função
            df2 = lambdify(x, diff(expressao, x, 2), "math")  # Segunda derivada da função
            resultado = newton(f, df, df2, a, b, tipo, erro, max_iter)
        elif metodo == "secante":
            resultado = secante(f, a, b, tipo, erro, max_iter)
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        print(f"\nErro: {e}")

    if resultado is not None:
        raiz, iteracoes = resultado
        n = casas_decimais(tipo, erro, raiz)
        print("\nResultado:")
        print(f"Raiz aproximada: {raiz:.{n}f}")
        print(f"f(raiz) = {f(raiz):.3e}")
        print(f"Número de iterações: {iteracoes}")
        if abs(f(raiz)) > 1e-3:  # Limite ajustável conforme necessário
            print("\nAviso: f(raiz) não é próximo de zero; o valor obtido provavelmente não é uma raiz.")

if __name__ == "__main__":
    main()
