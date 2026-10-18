
def bissecao(f, a, b, tipo, erro, max_iter):
    # Calcula f nos extremos uma só vez (evita repetir cálculos)
    fa, fb = f(a), f(b)

    # Se um extremo já for raiz, não é preciso iterar
    if fa == 0:
        return a, 0
    if fb == 0:
        return b, 0

    # Teorema de Bolzano: f(a) e f(b) devem ter sinais opostos para garantir que há uma raiz no intervalo
    if (fa > 0) == (fb > 0):
        print("f(a) e f(b) têm o mesmo sinal: não se garante zero neste intervalo.")
        continuar = input("Pretende continuar? (s/n): ").strip().lower()
        if continuar != "s":
            return None
        
    # Início do método da bissecção
    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        estimativa = (b - a) / 2
        if tipo == "r" and c != 0:
            estimativa = estimativa / abs(c) # Erro relativo: divide por |c|

        if fc == 0 or estimativa < erro:
            return c, i

        if (fa > 0) != (fc > 0):
            b, fb = c, fc #Atualiza o intervalo para [a, c]
        else:
            a, fa = c, fc #Atualiza o intervalo para [c, b]

    print(f"Atingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return c, max_iter
