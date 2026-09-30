from Utils import validacao_caracteres

def ler_input() -> tuple[int, str, int]:
    """
    Lê a entrada do usuário para a base de origem, o número e a base de destino.
    
    Returns:
        tuple: Uma tupla contendo a base de origem (int), o número (str) e a base de destino (int).

    """

    while True:
        try:
            base_atual = int(input("Insira a base atual (2 a 62): "))
        except ValueError:
                print("Base inválida. Por favor, insira um número inteiro entre 2 e 62.")
                continue
        
        if base_atual < 2 or base_atual > 62:
            print("Base inválida. Por favor, insira um número inteiro entre 2 e 62.")
            continue

        numero = input("Insira o número a ser convertido: ")

        if not validacao_caracteres(numero, base_atual):
            print("Número imcompatível com a base atual. Por favor, insira um número válido.")
            continue
        break

    while True:
        try:
            base_nova = int(input("Insira a base de destino (2 a 62): "))
        except ValueError:
            print("Base inválida. Por favor, insira um número inteiro entre 2 e 62.")
            continue
        
        if base_nova < 2 or base_nova > 62:
            print("Base inválida. Por favor, insira um número inteiro entre 2 e 62.")
            continue
        break

    return base_atual, numero, base_nova