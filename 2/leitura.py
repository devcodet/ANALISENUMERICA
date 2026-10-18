from sympy import symbols, lambdify, sympify
from traducao import traduzir

x = symbols("x")

def ler_numero(mensagem, positivo=False):
    while True:
        texto = input(mensagem).strip().replace(",", ".")

        try:
            numero = float(texto)
        except ValueError:
            print("Isso não é um número. Tente de novo.")
            continue
        if positivo and numero <= 0:
            print("O número tem de ser positivo. Tente de novo.")
            continue
        return numero

def ler_inteiro_positivo(mensagem):
    while True:
        texto = input(mensagem)

        try:
            numero = int(texto)
        except ValueError:
            print("Digite um número inteiro (ex: 50).")
            continue

        if numero <= 0:
            print("Tem de ser maior que 0.")
        else:
            return numero

def ler_funcao():
    while True:
        texto = input("Função/equação (ex.: x^3 - 2*x - 5  ou  cos(x) = x): ")
        texto = traduzir(texto.strip()).replace("==", "=")

        # Aceita também a notação "f(x) = ...", removendo o prefixo
        if texto.lower().startswith("f(x)"):
            texto = texto[4:].lstrip("= ")

        try:
            if texto.count("=") == 1:
                # É uma equação, então converte de esquerda = direita para esquerda - direita = 0
                esquerda, direita = texto.split("=")
                expressao = sympify(esquerda) - sympify(direita)
            else:
                # É uma função normal
                expressao = sympify(texto)

            # Só a variável x é permitida
            if expressao.free_symbols - {x}:
                print("Só pode usar a variável x.")
                continue

            f = lambdify(x, expressao, "math") # Converte para uma função Python que usa a biblioteca math
            return f, expressao
        except Exception:
            # Texto inválido (parênteses por fechar, nomes desconhecidos, etc.)
            print("Função inválida. Exemplo: x^3 - 2*x - 5")       

def ler_intervalo():
    while True:
        a = ler_numero("Início do intervalo (a): ")
        b = ler_numero("Fim do intervalo (b): ")

        if a < b:
            return a, b
        print("O início tem de ser menor que o fim.")


def ler_metodo():
    while True:
        print("1 - Bissecção")
        print("2 - Newton")
        print("3 - Secante")
        escolha = input("Método: ")

        if escolha == "1":
            return "bissecao"
        elif escolha == "2":
            return "newton"
        elif escolha == "3":
            return "secante"
        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

def ler_precisao_iteracoes():
    while True:
        tipo = input("Tipo de erro (a - absoluto, r - relativo): ").strip().lower()
        if tipo in ("a", "r"):
            break
        print("Digite 'a' ou 'r'.")
    erro = ler_numero("Erro pretendido (ex.: 1e-6): ", positivo=True)
    max_iter = ler_inteiro_positivo("Número máximo de iterações: ")
    return tipo, erro, max_iter
