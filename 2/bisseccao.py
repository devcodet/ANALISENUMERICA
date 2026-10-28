from utilitarios import cabecalho_tabela_bisseccao, fim_tabela_bisseccao, linha_tabela_bisseccao, verificar_bolzano, verificar_raiz_extremo, calcular_estimativa

def bissecao(f, a, b, tipo, erro, max_iter):

    r = verificar_raiz_extremo(f, a, b) # Verifica se f(a) ou f(b) é zero, o que significa que encontramos uma raiz exata
    if r is not None:
        return r
    if not verificar_bolzano(f, a, b): # Verifica se f(a) e f(b) têm sinais opostos
        return None                    # Se não tiverem, o método da bissecção não pode ser aplicado

    # f(a) é usado na decisão de que metade manter, então calculamos uma vez no início
    fa = f(a)

    cabecalho_tabela_bisseccao()  # Imprime o cabeçalho da tabela de iterações

    # Início do método da bissecção
    try:
        for i in range(1, max_iter + 1):
            c = (a + b) / 2
            fc = f(c)

            estimativa = calcular_estimativa(tipo, (b - a) / 2, c)  # Calcula a estimativa de erro com base no tipo escolhido

            linha_tabela_bisseccao(i, a, b, c, fc, estimativa)  # Imprime linha a linha a tabela de iterações

            if fc == 0 or estimativa < erro:
                return c, i  # Convergiu, logo retorna a raiz aproximada e o número de iterações

            if (fa > 0) != (fc > 0):
                b = c #Atualiza o intervalo para [a, c]
            else:
                a, fa = c, fc #Atualiza o intervalo para [c, b]
    finally:
        fim_tabela_bisseccao()  # Imprime a linha final da tabela de iterações - corre sempre: no return, no raise e ao fim do ciclo

    print(f"\nAtingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return c, max_iter
