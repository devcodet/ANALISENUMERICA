
def bissecao(f, a, b, tipo, erro, max_iter):
    # Calcula f nos extremos uma só vez (evita repetir cálculos)
    fa, fb = f(a), f(b)

    # Se um extremo já for raiz, não é preciso iterar
    if fa == 0:
        return a, 0
    if fb == 0:
        return b, 0

    if (fa > 0) == (fb > 0):
        print("f(a) e f(b) têm o mesmo sinal: não se garante zero neste intervalo.")
        continuar = input("Pretende continuar? (s/n): ").strip().lower()
        if continuar != "s":
            return None

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        estimativa = (b - a) / 2
        if tipo == "r" and c != 0:
            estimativa = estimativa / abs(c) # erro relativo: divide por |c|

        if fc == 0 or estimativa < erro:
            return c, i

        if (fa > 0) != (fc > 0):
            b, fb = c, fc
        else:
            a, fa = c, fc

    print(f"Atingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return c, max_iter
