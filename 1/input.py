import Numero

from Utilitarios import validacaoCaracteres


def lerInput() -> Numero:
    """
    Lê a entrada do usuário para a base de origem, o número e a base de destino.

    Returns:
        tuple: Uma tupla contendo a base de origem (int), o número (str) e a base de destino (int).

    """

    while True:
        try:
            base_atual = int(input("BASE ATUAL (2 a 62): "))
        except ValueError:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue

        if base_atual < 2 or base_atual > 62:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue

        numero = input("NUMERO: ")

        if not validacaoCaracteres(numero, base_atual):
            print(
                "Número incompatível com a base atual")
            continue
        break

    while True:
        try:
            base_nova = int(input("NOVA BASE (2 a 62): "))
        except ValueError:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue

        if base_nova < 2 or base_nova > 62:
            print("Base inválida. Insira um número inteiro entre 2 e 62.")
            continue
        break

    return Numero.Numero(base_atual, numero, base_nova, 0)
