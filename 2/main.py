from leitura import ler_funcao, ler_intervalo, ler_metodo, ler_precisao_iteracoes
from bisseccao import bissecao
from secante import secante
from newton import newton


def main():
    f, expressao = ler_funcao()
    a, b = ler_intervalo()
    metodo = ler_metodo()
    tipo, erro, max_iter = ler_precisao_iteracoes()

    resultado = None

    try:
        if metodo == "bissecao":
            resultado = bissecao(f, a, b, tipo, erro, max_iter)
        elif metodo == "newton":
            print("Newton ainda não está implementado.")
        elif metodo == "secante":
            resultado = secante(f, a, b, tipo, erro, max_iter)
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        print(f"Erro: {e}")

    if resultado is not None:
        raiz, iteracoes = resultado
        print(f"Raiz aproximada: {raiz}")
        print(f"f(raiz) = {f(raiz):.3e}")
        print(f"Número de iterações: {iteracoes}")

if __name__ == "__main__":
    main()
    