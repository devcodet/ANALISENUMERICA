from utilitarios import cabecalho_tabela, fim_tabela, linha_tabela, verificar_bolzano, verificar_raiz_extremo, perguntar_continuar, calcular_estimativa

def secante(f, a, b, tipo, erro, max_iter):

    r = verificar_raiz_extremo(f, a, b) # Verifica se f(a) ou f(b) é zero, o que significa que encontramos uma raiz exata
    if r is not None:
        return r
    if not verificar_bolzano(f, a, b) and not perguntar_continuar(): # Verifica se f(a) e f(b) têm sinais opostos e pergunta se o usuário quer continuar
        return None                                                  # Caso não tiverem, desiste do método se o usuário não quiser continuar

    r_menos1, r0 = a, b  # Pontos iniciais para o método da secante
    f_r_menos1, f_r0 = f(a), f(b) # Calcula f nos extremos uma só vez (evita repetir cálculos)

    if f_r0 - f_r_menos1 == 0: # Mostra o erro antes de entrar no loop, caso os pontos iniciais sejam iguais ou a reta secante seja horizontal
        raise ValueError(f"f(r-1) = f(r0) = {f_r0:.6g}: a reta secante é horizontal e a fórmula divide por zero.")

    cabecalho_tabela()  # Imprime o cabeçalho da tabela de iterações

    # Início do método da secante
    try:
        for i in range(1, max_iter + 1):
            if f_r0 - f_r_menos1 == 0:
                raise ValueError(f"f(r-1) = f(r0): a reta secante é horizontal e a fórmula divide por zero na iteração {i}.")
        
            # Fórmula da secante
            r1 = r0 - f_r0 * (r0 - r_menos1) / (f_r0 - f_r_menos1)
        
            estimativa = calcular_estimativa(tipo, r1 - r0, r1)

            f_r1 = f(r1)

            linha_tabela(i, r1, f_r1, estimativa)  # Imprime linha a linha a tabela de iterações

            if f_r1 == 0 or estimativa < erro:
                return r1, i  # Convergiu, logo retorna a raiz aproximada e o número de iterações
        
            # Atualiza os pontos para a próxima iteração
            r_menos1, f_r_menos1 = r0, f_r0
            r0, f_r0 = r1, f_r1
    finally:
        fim_tabela()  # Imprime a linha final da tabela de iterações - corre sempre: no return, no raise e ao fim do ciclo
    
    print(f"\nAtingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return r1, max_iter
