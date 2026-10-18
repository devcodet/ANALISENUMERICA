
def secante(f, x0, x1, tipo, erro, max_iter):
    # Calcula f nos extremos uma só vez (evita repetir cálculos)
    f0, f1 = f(x0), f(x1)

    # Início do método da secante
    for i in range(1, max_iter + 1):
        if f1 - f0 == 0:
            raise ValueError("f(x0) = f(x1): divisão por zero na fórmula da secante.")
        
        # Fórmula da secante
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        
        estimativa = abs(x2 - x1)
        if tipo == "r" and x2 != 0:
            estimativa = estimativa / abs(x2)

        f2 = f(x2)
        if f2 == 0 or estimativa < erro:
            return x2, i  # Retorna a raiz aproximada e o número de iterações
        
        # Atualiza os pontos para a próxima iteração
        x0, f0 = x1, f1
        x1, f1 = x2, f2
    
    print(f"Atingiu o máximo de {max_iter} iterações sem chegar ao erro pedido.")
    return x2, max_iter
