from input import ler_funcao, ler_intervalo, ler_metodo, ler_precisao_iteracoes
from bisseccao import bissecao


def main():
    f, expressao = ler_funcao()
    a, b = ler_intervalo()
    metodo = ler_metodo()
    tipo, erro, max_iter = ler_precisao_iteracoes()

    resultado = None

    if metodo == "bissecao":
        resultado = bissecao(f, a, b, tipo, erro, max_iter)
    elif metodo == "newton":
        #falta fazer o newton
        pass
    elif metodo == "secante":
        #falta fazer a secante
        pass

    if resultado is not None:
        raiz, iteracoes = resultado
        print(f"Raiz aproximada: {raiz}")
        print(f"Número de iterações: {iteracoes}")

if __name__ == "__main__":
    main()