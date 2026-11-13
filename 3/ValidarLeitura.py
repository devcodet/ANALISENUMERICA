
def validar_vetor(vetor: list[float], tamanho: int) -> bool:

    if len(vetor) != tamanho:
        raise ValueError(f"Erro: O vetor deve ter exatamente {tamanho} elementos. Tamanho atual: {len(vetor)}.")

    for valor in vetor:
        if not isinstance(valor, (int, float)):
            raise ValueError(f"Erro: O valor '{valor}' não é um número válido.")

def validar_matriz(matriz: list[list[float]], n: int) -> bool:

    if len(matriz) != n:
        raise ValueError(f"Erro: A matriz deve ter exatamente {n} linhas. Linhas atuais: {len(matriz)}.")

    for i, linha in enumerate(matriz):
        if len(linha) != n:
            raise ValueError(f"Erro: A linha {i + 1} da matriz deve ter exatamente {n} colunas. Colunas atuais: {len(linha)}.")
        for valor in linha:
            if not isinstance(valor, (int, float)):
                raise ValueError(f"Erro: O valor '{valor}' na linha {i + 1} não é um número válido.")

def validar_tamanho_matriz(n: int) -> bool:

        if not n.isdigit():
            raise ValueError("Erro: Insira apenas números inteiros positivos.")

        n = int(n)

        if n <= 0:
            raise ValueError("Erro: O número de linhas e colunas deve ser maior que zero.")