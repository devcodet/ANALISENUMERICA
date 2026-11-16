from ValidarLeitura import converter_para_float, validar_matriz, validar_vetor, validar_tamanho_matriz
import numpy


# Funções de leitura de dados do usuário

def ler_numero(mensagem, positivo=False) -> float:
    while True:
        texto = input(mensagem).strip()

        try:
            numero = converter_para_float(texto)
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

def ler_tamanho_matriz() -> int:

    while True:

        n = input("\nInsira o número de equações e incógnitas do sistema(linhas e colunas da matriz):").strip()

        try:
            return validar_tamanho_matriz(n)
        except ValueError as e:
            print(f"\nFormato inválido: {e}")

def ler_matriz(n: int) -> list[list[float]]:

    matriz: list[list[float]] = numpy.zeros((n, n)).tolist()

    for i in range(n):
        while True:
            linha = input(f"\nInsira os {n} valores da linha {i + 1} da matriz dos coeficientes A, separados por ';': ").strip().split(';')

            if len(linha) != n:
                print(f"\nErro: Insira exatamente {n} valores.")
                continue

            try:
                matriz[i] = [converter_para_float(valor) for valor in linha]
                validar_matriz(matriz, n)
                break
            except ValueError as e:
                print(f"\nMatriz inválida. {e}. Tente novamente.")  

    return matriz 

def ler_vetor(tamanho: int, descricao: str = "do vetor dos termos independentes B") -> list[float]:

    while True:
        linha = input(f"\nInsira os {tamanho} valores {descricao}, separados por ';': ").strip().split(';')

        if len(linha) != tamanho:
            print(f"\nErro: Insira exatamente {tamanho} valores.")
            continue

        try:
            vetor = [converter_para_float(valor) for valor in linha]
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

def ler_tolerancia_iteracoes() -> tuple[str, str, float, int]:
    while True:
        tipo_erro = input("Tipo de erro (a - absoluto, r - relativo): ").strip().lower()
        if tipo_erro in ("a", "r"):
            break
        print("\nDigite 'a' ou 'r'.")

    while True:
        tipo_norma = input("Tipo de norma utilizada (s - soma, e - euclidiana, m - do máximo): ").strip().lower()
        if tipo_norma in ("s", "e", "m"):
            break
        print("\nDigite 's', 'e' ou 'm'.")
        
    tolerancia = ler_numero("Tolerância pretendida (ex.: 1e-6): ", positivo=True)
    max_iter = ler_inteiro_positivo("Número máximo de iterações: ")

    return tipo_erro, tipo_norma, tolerancia, max_iter
