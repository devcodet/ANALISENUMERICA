from ValidarLeitura import validar_matriz, validar_vetor, validar_tamanho_matriz


# Funções de leitura de dados do usuário

def ler_numero(mensagem, positivo=False) -> float:
    while True:
        texto = input(mensagem).strip().replace(",", ".")

        try:
            numero = float(texto)
        except ValueError:
            print("\nIsso não é um número. Tente de novo.")
            continue
        if positivo and numero <= 0:
            print("\nO número tem de ser positivo. Tente de novo.")
            continue
        return numero

def ler_inteiro_positivo(mensagem) -> int:
    while True:
        texto = input(mensagem)

        try:
            numero = int(texto)
        except ValueError:
            print("\nDigite um número inteiro (ex: 50).")
            continue

        if numero <= 0:
            print("\nTem de ser maior que 0.")
        else:
            return numero

def tamanho_matriz() -> int:

    while True:

        n = input("\nInsira o número de equações e incógnitas do sistema(linhas da matriz):").strip()

        try:
            n = validar_tamanho_matriz(n)
        except ValueError as e:
            print(f"\nFormato inválido: {e}")
            continue

        return n

def ler_matriz(linhas: int, colunas: int) -> list[list[float]]:

    matriz: list[list[float]] = [[0.0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        while True:
            linha = input(f"\nInsira os {colunas} valores da linha {i + 1} da matriz dos coeficientes A, separados por espaço: ").strip().split()

            if len(linha) != colunas:
                print(f"\nErro: Insira exatamente {colunas} valores.")
                continue

            try:
                matriz[i] = [float(valor) for valor in linha]
                validar_matriz(matriz, linhas, colunas)
                break
            except ValueError as e:
                print(f"\nMatriz inválida. {e}. Tente novamente.")  

    return matriz 

def ler_vetor(tamanho: int) -> list[float]:

    while True:
        linha = input(f"\nInsira os {tamanho} valores do vetor dos termos independentes B, separados por espaço: ").strip().split()

        if len(linha) != tamanho:
            print(f"\nErro: Insira exatamente {tamanho} valores.")
            continue

        try:
            vetor = [float(valor) for valor in linha]
            validar_vetor(vetor, tamanho)
            break
        except ValueError as e:
            print(f"\nVetor inválido. {e}. Tente novamente.")

    return vetor

def ler_metodo() -> str:
    while True:
        print("1 - Método iterativo de Jacobi")
        print("2 - Método iterativo de Gauss-Seidel")
        escolha = input("Método: ")

        if escolha == "1":
            return "Jacobi"
        elif escolha == "2":
            return "Gauss-Seidel"
        else:
            print("\nOpção inválida. Digite 1 ou 2.")

def ler_tolerancia_iteracoes() -> tuple[str, float, int]:
    while True:
        tipo = input("Tipo de erro (a - absoluto, r - relativo): ").strip().lower()
        if tipo in ("a", "r"):
            break
        print("\nDigite 'a' ou 'r'.")
        
    tolerancia = ler_numero("Tolerância pretendida (ex.: 1e-6): ", positivo=True)
    max_iter = ler_inteiro_positivo("Número máximo de iterações: ")

    return tipo, tolerancia, max_iter