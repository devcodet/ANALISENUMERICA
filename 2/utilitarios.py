import math

TRADUCOES = {
    # seno
    "seno": "sin", "sen": "sin", "sine": "sin",
    # cosseno
    "cosseno": "cos", "coseno": "cos", "cosine": "cos",
    # tangente
    "tangente": "tan", "tangent": "tan", "tg": "tan",
    # secante
    "secante": "sec", "secant": "sec",
    # cossecante
    "cossecante": "csc", "cosecante": "csc", "cosecant": "csc", "cscante": "csc",
    # cotangente
    "cotangente": "cot", "cotangent": "cot", "ctg": "cot",
    # logaritmo natural
    "ln": "log", "Ln": "log", "LN": "log",
    "logn": "log", "Log": "log", "LOG": "log",
    # número de Euler (só na forma e^x)
    "e**": "E**",
}

ALGARISMOS = 14 # Nº de algarimos usados na tabela

def traduzir(texto):
    texto = texto.replace("^", "**")
    for antigo in sorted(TRADUCOES, key=len, reverse=True):
        texto = texto.replace(antigo, TRADUCOES[antigo])
    return texto

def verificar_bolzano(f, a, b): # Pressupõe que f seja contínua no intervalo [a, b]
    # Teorema de Bolzano: f(a) e f(b) devem ter sinais opostos para garantir que há uma raiz no intervalo
    fa, fb = f(a), f(b)

    if fa == 0 or fb == 0:
        return True  # Se f(a) ou f(b) for zero, encontramos uma raiz exata
    if (fa > 0) == (fb > 0):
        print("\nf(a) e f(b) têm o mesmo sinal: não se garante zero neste intervalo.")
        return False
    return True

def verificar_raiz_extremo(f, a, b):
    # Verifica se f(a) ou f(b) é zero, o que significa que encontramos uma raiz exata
    fa, fb = f(a), f(b)

    if fa == 0:
        print(f"f({a}) = 0: O extremo {a} é uma raiz exata.")
        return a, 0
    elif fb == 0:
        print(f"f({b}) = 0: O extremo {b} é uma raiz exata.")
        return b, 0
    return None

def perguntar_continuar():
    # True se o usuário quiser continuar, False caso contrário
    while True:
        resposta = input("\nPretende continuar? (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return True if resposta == "s" else False
        print("\nResposta inválida. Digite 's' para sim ou 'n' para não.")

def calcular_estimativa(tipo, diferenca, valor):
    # Erro absoluto = |diferenca|; relativo = |diferenca| / |valor| (se valor != 0)
    estimativa = abs(diferenca)
    if tipo == "r" and valor != 0:
        estimativa /= abs(valor)
    return estimativa

def casas_decimais(tipo, erro, raiz):
    # Nº de casas decimais coerente com o erro pedido
    
    erro_abs = erro if tipo == "a" else erro * abs(raiz) # Com tipo = "r", "erro" é uma proporção de |raiz| e não uma distância.
                                                         # Para saber quantas são as casas decimais fiáveis, converte-se para erro absoluto
        
    # Raiz = 0 com erro relativo dá erro_abs = 0 e o log10 falharia, logo usa-se 10 casas
    if erro_abs <= 0:
        return 10

    n = max(0, math.ceil(-math.log10(erro_abs)))
    return min(n, 15)

# Funções para imprimir tabelas de iterações

def cabecalho_tabela():
    print()
    print("=" * 49)
    print(f"{'i':>3}  {'x':>18}  {'f(x)':>11}  {'erro':>11}")
    print("-" * 49)

def linha_tabela(i, x, fx, estimativa):
    print(f"{i:3d}  {x:18.{ALGARISMOS}g}  {fx:11.3e}  {estimativa:11.3e}")

def cabecalho_tabela_bisseccao():
    print()
    print("=" * 89)
    print(f"{'i':>3}  {'a':>18}  {'b':>18}  {'c':>18}  {'f(c)':>11}  {'erro':>11}")
    print("-" * 89)

def linha_tabela_bisseccao(i, a, b, c, fc, estimativa):
    print(f"{i:3d}  {a:18.{ALGARISMOS}g}  {b:18.{ALGARISMOS}g}  {c:18.{ALGARISMOS}g}  {fc:11.3e}  {estimativa:11.3e}")

def fim_tabela():
    print("=" * 49)

def fim_tabela_bisseccao():
    print("=" * 89)

        


