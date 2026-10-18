
def newton(f, df, x0, tipo, erro, max_iter):

    # Início do método de Newton
    for i in range(1, max_iter + 1):
        d = df(x0)
        if d == 0:
            raise ValueError("Derivada nula: o método de Newton falha neste ponto.")

        # Fórmula de Newton
        x1 = x0 - f(x0) / d

        estimativa = abs(x1 - x0)
        if tipo == "r" and x1 != 0:
            estimativa = estimativa / abs(x1)

        f1 = f(x1)

        if f1 == 0 or estimativa < erro:
            return x1, i  # Retorna a raiz aproximada e o número de iterações

        x0 = x1  # Atualiza o ponto para a próxima iteração

    print(f"Atingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return x1, max_iter
