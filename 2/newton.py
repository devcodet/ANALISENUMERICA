from utilitarios import cabecalho_tabela, fim_tabela, linha_tabela, verificar_bolzano, verificar_raiz_extremo, perguntar_continuar, calcular_estimativa

def newton(f, df, df2, a, b, tipo, erro, max_iter):

    r = verificar_raiz_extremo(f, a, b) # Verifica se f(a) ou f(b) é zero, o que significa que encontramos uma raiz exata
    if r is not None:
        return r
    if not verificar_bolzano(f, a, b) and not perguntar_continuar(): # Verifica se f(a) e f(b) têm sinais opostos e pergunta se o usuário quer continuar
        return None                                                  # Caso não tiverem, desiste do método se o usuário não quiser continuar

    # Escolha do extremo favorável
    if f(a) * df2(a) > 0:
        r0 = a
    elif f(b) * df2(b) > 0:
        r0 = b
    else:
        print("\nAviso: nenhum extremo verifica f x f'' > 0; usa-se b como ponto inicial.")
        r0 = b

    if df(r0) == 0: # Mostra o erro antes de entrar no loop, caso o ponto inicial seja um ponto crítico
        raise ValueError(f"Derivada nula no ponto inicial r0 = {r0:.6g}: o método de Newton falha.")
    
    cabecalho_tabela()  # Imprime o cabeçalho da tabela de iterações

    # Início do método de Newton
    try:
        for i in range(1, max_iter + 1):
            d = df(r0)
            if d == 0:
                raise ValueError(f"Derivada nula na iteração {i}: o método de Newton falha neste ponto.")

            # Fórmula de Newton
            r1 = r0 - f(r0) / d

            estimativa = calcular_estimativa(tipo, r1 - r0, r1)
        
            f_r1 = f(r1)

            linha_tabela(i, r1, f_r1, estimativa)  # Imprime linha a linha a tabela de iterações

            if f_r1 == 0 or estimativa < erro:
                return r1, i  # Convergiu, logo retorna a raiz aproximada e o número de iterações

            r0 = r1  # Atualiza o ponto para a próxima iteração
    finally:
        fim_tabela()  # Imprime a linha final da tabela de iterações - corre sempre: no return, no raise e ao fim do ciclo

    print(f"\nAtingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return r1, max_iter
