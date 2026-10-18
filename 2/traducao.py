
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

def traduzir(texto):
    texto = texto.replace("^", "**")
    for antigo in sorted(TRADUCOES, key=len, reverse=True):
        texto = texto.replace(antigo, TRADUCOES[antigo])
    return texto
